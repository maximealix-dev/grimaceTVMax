# 📺 Grimace TV - Application Streamlit

Une application fun pour partager et afficher des grimaces amusantes !

## 🚀 Installation Locale

1. **Installez les dépendances :**
```bash
pip install -r requirements.txt
```

2. **Lancez l'application :**
```bash
streamlit run app.py
```

3. **Ouvrez votre navigateur :**
L'application s'ouvrira automatiquement à l'adresse : `http://localhost:8501`

## ☁️ Déploiement sur Streamlit Cloud

### Méthode 1 : Via GitHub (Recommandée)

1. **Créez un compte sur [Streamlit Cloud](https://streamlit.io/cloud)**

2. **Créez un repository GitHub avec ces fichiers :**
   - `app.py` (l'application principale)
   - `requirements.txt` (les dépendances)
   - `README.md` (ce fichier)

3. **Déployez sur Streamlit Cloud :**
   - Connectez-vous à [share.streamlit.io](https://share.streamlit.io)
   - Cliquez sur "New app"
   - Sélectionnez votre repository GitHub
   - Branch : `main` (ou `master`)
   - Main file path : `app.py`
   - Cliquez sur "Deploy!"

4. **Votre app sera accessible via une URL publique** (ex: `https://votre-app.streamlit.app`)

### Méthode 2 : Autres plateformes

#### Heroku
```bash
# Ajoutez un fichier Procfile
web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

#### Railway.app
- Importez votre repository GitHub
- Railway détectera automatiquement Streamlit
- L'app sera déployée automatiquement

## 📝 Fonctionnalités

- **📸 Envoi de grimaces** : Uploadez une photo avec votre prénom, âge et commentaire
- **📺 Galerie TV** : Visualisez toutes les grimaces en mode grille
- **🔄 Auto-actualisation** : Rafraîchissez pour voir les nouvelles grimaces
- **🗑️ Gestion** : Effacez toutes les grimaces d'un clic

## 🎨 Personnalisation

Vous pouvez modifier les couleurs dans le CSS de `app.py` :
- `--primary: #FF6B35` (orange principal)
- `--secondary: #F7931E` (orange secondaire)
- `--accent: #FDC500` (jaune accent)

## 💾 Stockage des données

Les grimaces sont stockées dans un fichier `grimaces_data.json` qui est créé automatiquement au premier lancement.

**Note :** Sur Streamlit Cloud, ce fichier sera temporaire et sera réinitialisé à chaque redéploiement. Pour une solution permanente, considérez l'utilisation d'une base de données externe (Firebase, MongoDB, etc.).

## 🔧 Configuration avancée

Pour configurer Streamlit, créez un fichier `.streamlit/config.toml` :

```toml
[theme]
primaryColor = "#FF6B35"
backgroundColor = "#FFE5D9"
secondaryBackgroundColor = "#FFF8E7"
textColor = "#2C1810"
font = "sans serif"

[server]
maxUploadSize = 10
```

## 📱 Responsive

L'application est responsive et fonctionne sur :
- 💻 Desktop
- 📱 Tablette
- 📲 Mobile

## 🎭 Crédits

Créé avec ❤️ en utilisant Streamlit et Python
Fonts : Bangers & Fredoka de Google Fonts

---

**Amusez-vous bien avec Grimace TV ! 😜🎉**
