# 🚀 Guide Rapide de Déploiement

## Commandes à Exécuter (Copier-Coller)

### 1️⃣ Ouvrir PowerShell dans le dossier du projet

```powershell
cd C:\Users\MSI\Desktop\ESPRIT_COURS_4EME\ML\sante_plus_app
```

### 2️⃣ Initialiser Git

```powershell
git init
git add .
git commit -m "Initial commit - Santé Plus Streamlit app"
git branch -M main
```

### 3️⃣ Créer le repository sur GitHub

1. Allez sur **https://github.com**
2. Cliquez sur **"+"** → **"New repository"**
3. Nom : `sante-plus-app`
4. **Ne cochez PAS** "Initialize with README"
5. Cliquez **"Create repository"**

### 4️⃣ Connecter et Pousser sur GitHub

**Remplacez `VOTRE_USERNAME` par votre nom d'utilisateur GitHub :**

```powershell
git remote add origin https://github.com/VOTRE_USERNAME/sante-plus-app.git
git push -u origin main
```

Si GitHub vous demande vos identifiants :
- **Username** : Votre nom d'utilisateur GitHub
- **Password** : Utilisez un **Personal Access Token** (pas votre mot de passe)
  - Créer un token : GitHub → Settings → Developer settings → Personal access tokens → Generate new token

### 5️⃣ Déployer sur Streamlit Cloud

1. Allez sur **https://share.streamlit.io/**
2. Cliquez sur **"Sign in"** → Connectez-vous avec GitHub
3. Cliquez sur **"New app"**
4. Sélectionnez :
   - **Repository** : `sante-plus-app`
   - **Branch** : `main`
   - **Main file path** : `app.py`
5. Cliquez sur **"Deploy"**
6. Attendez 2-5 minutes
7. **C'est fait !** 🎉 Votre app est en ligne !

## ⚡ Commandes Rapides pour les Mises à Jour

Après chaque modification de code :

```powershell
git add .
git commit -m "Description de vos modifications"
git push
```

Streamlit Cloud redéploiera automatiquement !

## ❓ Problèmes Courants

### "Git n'est pas reconnu"
→ Installez Git : https://git-scm.com/downloads

### "Repository already exists"
→ Le repo existe déjà sur GitHub, utilisez :
```powershell
git remote set-url origin https://github.com/VOTRE_USERNAME/sante-plus-app.git
git push -u origin main
```

### "Permission denied"
→ Vérifiez votre nom d'utilisateur GitHub et utilisez un Personal Access Token

---

**Bon déploiement ! 🚀**

