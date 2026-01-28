import streamlit as st
import json
import os
from datetime import datetime
from PIL import Image
import base64
from io import BytesIO

# Configuration de la page
st.set_page_config(
    page_title="Grimace TV",
    page_icon="📺",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Fichier JSON pour stocker les grimaces
GRIMACES_FILE = "grimaces_data.json"

# Initialiser le fichier s'il n'existe pas
if not os.path.exists(GRIMACES_FILE):
    with open(GRIMACES_FILE, 'w') as f:
        json.dump([], f)

# Fonction pour charger les grimaces
def load_grimaces():
    try:
        with open(GRIMACES_FILE, 'r') as f:
            return json.load(f)
    except:
        return []

# Fonction pour sauvegarder les grimaces
def save_grimaces(grimaces):
    with open(GRIMACES_FILE, 'w') as f:
        json.dump(grimaces, f, indent=2)

# Fonction pour convertir une image en base64
def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Initialiser session_state
if 'refresh_key' not in st.session_state:
    st.session_state.refresh_key = 0

# CSS personnalisé pour le style Grimace TV
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600;700&family=Bangers&display=swap');
    
    /* Cacher le menu Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Style général */
    .stApp {
        background: linear-gradient(135deg, #FFE5D9 0%, #FFC2D1 50%, #D4A5FF 100%);
        font-family: 'Fredoka', sans-serif;
    }
    
    /* Titre principal */
    .main-title {
        font-family: 'Bangers', cursive;
        font-size: 4rem;
        color: #FF6B35;
        text-align: center;
        text-shadow: 4px 4px 0 #F7931E, 8px 8px 0 #FDC500;
        letter-spacing: 0.1em;
        margin-bottom: 1rem;
        animation: bounce 2s infinite;
    }
    
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }
    
    /* Carte de grimace */
    .grimace-card {
        background: white;
        border-radius: 20px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
    }
    
    .grimace-card:hover {
        transform: scale(1.02);
        box-shadow: 0 15px 40px rgba(255, 107, 53, 0.3);
    }
    
    .grimace-name {
        font-family: 'Bangers', cursive;
        font-size: 2rem;
        color: #FF6B35;
        margin-bottom: 0.5rem;
    }
    
    .grimace-age {
        font-size: 1.2rem;
        color: #F7931E;
        font-weight: 600;
    }
    
    .grimace-comment {
        background: rgba(255, 107, 53, 0.1);
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #FF6B35;
        font-style: italic;
        margin: 1rem 0;
    }
    
    .grimace-date {
        color: #666;
        font-size: 0.9rem;
        text-align: right;
    }
    
    /* Boutons */
    .stButton > button {
        background: linear-gradient(135deg, #FF6B35 0%, #F7931E 100%);
        color: white;
        border: none;
        border-radius: 15px;
        padding: 0.8rem 2rem;
        font-family: 'Fredoka', sans-serif;
        font-weight: 600;
        font-size: 1.1rem;
        box-shadow: 0 5px 15px rgba(255, 107, 53, 0.3);
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(255, 107, 53, 0.5);
    }
    
    /* Champs de formulaire */
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input,
    .stTextArea > div > div > textarea {
        border: 3px solid #FF6B35 !important;
        border-radius: 10px !important;
        background: #FFF8E7 !important;
        font-family: 'Fredoka', sans-serif !important;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
        background: rgba(255, 255, 255, 0.5);
        border-radius: 15px;
        padding: 1rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        font-family: 'Fredoka', sans-serif;
        font-weight: 600;
        font-size: 1.2rem;
        border-radius: 10px;
        color: #FF6B35;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #FF6B35 0%, #F7931E 100%);
        color: white !important;
    }
    
    div[data-testid="stImage"] {
        border-radius: 15px;
        overflow: hidden;
    }
</style>
""", unsafe_allow_html=True)

# En-tête
st.markdown('<h1 class="main-title">📺 GRIMACE TV 📺</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; font-size: 1.5rem; color: #FF6B35; font-weight: 600; margin-bottom: 2rem;">Le Show des Grimaces les Plus Folles !</p>', unsafe_allow_html=True)

# Création des onglets
tab1, tab2 = st.tabs(["📸 ENVOYER UNE GRIMACE", "📺 VOIR LES GRIMACES"])

# Onglet 1: Envoyer une grimace
with tab1:
    st.markdown("### 🎭 Partagez votre meilleure grimace !")
    
    with st.form("grimace_form", clear_on_submit=True):
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Upload de photo
            uploaded_file = st.file_uploader(
                "📸 Choisissez votre photo de grimace",
                type=['png', 'jpg', 'jpeg'],
                help="Glissez-déposez votre photo ou cliquez pour parcourir"
            )
            
            if uploaded_file is not None:
                image = Image.open(uploaded_file)
                st.image(image, caption="Aperçu de votre grimace", use_container_width=True)
        
        with col2:
            # Formulaire
            st.markdown("#### Vos infos :")
            name = st.text_input("🏷️ Prénom / Pseudo", placeholder="Ex: SuperGrimaceur")
            age = st.number_input("🎂 Âge", min_value=1, max_value=120, value=25)
            comment = st.text_area(
                "💬 P'tit commentaire cool",
                placeholder="Ex: Ma grimace de champion du monde !",
                height=100
            )
        
        st.markdown("####")
        submitted = st.form_submit_button("🚀 ENVOYER MA GRIMACE !", use_container_width=True)
        
        if submitted:
            if uploaded_file is None:
                st.error("⚠️ Veuillez ajouter une photo !")
            elif not name:
                st.error("⚠️ Veuillez entrer votre prénom/pseudo !")
            elif not comment:
                st.error("⚠️ Veuillez ajouter un commentaire !")
            else:
                # Sauvegarder la grimace
                grimaces = load_grimaces()
                
                # Convertir l'image en base64
                image = Image.open(uploaded_file)
                image_b64 = image_to_base64(image)
                
                new_grimace = {
                    "name": name,
                    "age": age,
                    "comment": comment,
                    "image": image_b64,
                    "timestamp": datetime.now().isoformat()
                }
                
                grimaces.append(new_grimace)
                save_grimaces(grimaces)
                
                st.success("🎉 Grimace envoyée avec succès ! Allez voir l'onglet TV !")
                st.balloons()

# Onglet 2: Voir les grimaces
with tab2:
    grimaces = load_grimaces()
    
    # Barre de contrôle
    col1, col2, col3 = st.columns([1, 1, 3])
    with col1:
        if st.button("🔄 Actualiser", use_container_width=True):
            st.session_state.refresh_key += 1
            st.rerun()
    with col2:
        if st.button("🗑️ Tout Effacer", use_container_width=True):
            save_grimaces([])
            st.session_state.refresh_key += 1
            st.rerun()
    
    st.markdown("---")
    
    if len(grimaces) == 0:
        st.markdown("""
        <div style="text-align: center; padding: 5rem 2rem;">
            <div style="font-size: 5rem; margin-bottom: 1rem;">😢</div>
            <div style="font-size: 2rem; font-weight: 700; color: #FDC500; margin-bottom: 1rem;">
                Aucune grimace pour le moment !
            </div>
            <p style="color: #888; font-size: 1.2rem;">Soyez le premier à partager votre grimace !</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        # Affichage en grille
        cols_per_row = 2
        for idx in range(0, len(grimaces), cols_per_row):
            cols = st.columns(cols_per_row)
            for col_idx, col in enumerate(cols):
                grimace_idx = idx + col_idx
                if grimace_idx < len(grimaces):
                    grimace = grimaces[grimace_idx]
                    
                    with col:
                        # Conteneur de carte
                        st.markdown('<div class="grimace-card">', unsafe_allow_html=True)
                        
                        # En-tête avec nom et âge
                        st.markdown(f'<div class="grimace-name">{grimace["name"]}</div>', unsafe_allow_html=True)
                        st.markdown(f'<div class="grimace-age">🎂 {grimace["age"]} ans</div>', unsafe_allow_html=True)
                        
                        # Image
                        image_data = base64.b64decode(grimace["image"])
                        image = Image.open(BytesIO(image_data))
                        st.image(image, use_container_width=True)
                        
                        # Commentaire
                        st.markdown(f'<div class="grimace-comment">💬 "{grimace["comment"]}"</div>', unsafe_allow_html=True)
                        
                        # Date
                        date_obj = datetime.fromisoformat(grimace["timestamp"])
                        date_str = date_obj.strftime("%d/%m/%Y à %H:%M")
                        st.markdown(f'<div class="grimace-date">📅 Envoyé le {date_str}</div>', unsafe_allow_html=True)
                        
                        st.markdown('</div>', unsafe_allow_html=True)
                        st.markdown("<br>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; color: #666; font-size: 0.9rem;">
    <p>🎨 Grimace TV - Partagez vos grimaces les plus folles ! 🎭</p>
</div>
""", unsafe_allow_html=True)
