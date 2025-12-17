# Guide de Déploiement - Santé Plus

## 📋 Prérequis

- Compte GitHub
- Git installé sur votre machine
- Application testée et fonctionnelle localement

## 🚀 Étapes de Déploiement

### Étape 1 : Préparer le projet pour GitHub

1. **Vérifier que tous les fichiers sont présents** :
   - ✅ `app.py` (fichier principal)
   - ✅ `requirements.txt` (dépendances)
   - ✅ `style.css` (styles CSS)
   - ✅ Dossier `pages/` (toutes les pages)
   - ✅ Dossier `models/` (tous les modèles .pkl)
   - ✅ Dossier `data/` (si nécessaire)
   - ✅ `.gitignore` (créé automatiquement)

### Étape 2 : Initialiser Git et pousser sur GitHub

**Dans le terminal (PowerShell ou CMD), naviguez vers votre dossier projet :**

```bash
cd C:\Users\MSI\Desktop\ESPRIT_COURS_4EME\ML\sante_plus_app
```

**Initialiser Git :**
```bash
git init
```

**Ajouter tous les fichiers :**
```bash
git add .
```

**Créer le premier commit :**
```bash
git commit -m "Initial commit - Santé Plus Streamlit app"
```

**Renommer la branche en main :**
```bash
git branch -M main
```

**Créer le repository sur GitHub :**
1. Allez sur https://github.com
2. Cliquez sur le bouton "+" en haut à droite
3. Sélectionnez "New repository"
4. Nommez-le : `sante-plus-app`
5. **Ne cochez PAS** "Initialize with README"
6. Cliquez sur "Create repository"

**Ajouter le remote et pousser :**
```bash
git remote add origin https://github.com/VOTRE_USERNAME/sante-plus-app.git
git push -u origin main
```

⚠️ **Remplacez `VOTRE_USERNAME` par votre nom d'utilisateur GitHub !**

### Étape 3 : Déployer sur Streamlit Cloud

1. **Aller sur Streamlit Cloud** :
   - Visitez : https://share.streamlit.io/
   - Cliquez sur "Sign in" et connectez-vous avec votre compte GitHub

2. **Créer une nouvelle app** :
   - Cliquez sur "New app"
   - Sélectionnez votre repository : `sante-plus-app`
   - Sélectionnez la branche : `main`

3. **Configurer le déploiement** :
   - **Main file path** : `app.py`
   - **Python version** : Laisser par défaut (3.11 généralement)
   - Cliquez sur "Deploy"

4. **Attendre le déploiement** :
   - Streamlit va installer les dépendances depuis `requirements.txt`
   - Cela peut prendre 2-5 minutes
   - Vous verrez les logs en temps réel

5. **Votre application est en ligne !** 🎉
   - Vous recevrez un lien public du type : `https://sante-plus-app-xxxxx.streamlit.app`
   - Partagez ce lien avec qui vous voulez !

## 🔧 Résolution de Problèmes

### Erreur : "Module not found"
- Vérifiez que toutes les dépendances sont dans `requirements.txt`
- Vérifiez les versions de Python (Streamlit Cloud utilise Python 3.11)

### Erreur : "File not found" pour les modèles
- Assurez-vous que tous les fichiers `.pkl` sont dans le dossier `models/`
- Vérifiez que les chemins dans le code sont relatifs (ex: `models/svm.pkl`)

### Erreur : "Git not recognized"
- Installez Git : https://git-scm.com/downloads
- Redémarrez le terminal après l'installation

### Les modifications ne s'affichent pas
- Après chaque modification, faites :
  ```bash
  git add .
  git commit -m "Description des changements"
  git push
  ```
- Streamlit Cloud redéploiera automatiquement

## 📝 Notes Importantes

- ⚠️ **Les fichiers de modèles (.pkl) peuvent être volumineux**
  - Si GitHub refuse les fichiers > 100MB, vous devrez utiliser Git LFS
  - Ou héberger les modèles ailleurs (Google Drive, S3, etc.)

- 🔒 **Sécurité** :
  - Ne commitez JAMAIS de mots de passe ou clés API
  - Utilisez `.env` pour les variables sensibles (et ajoutez `.env` au `.gitignore`)

- 💰 **Gratuit** :
  - Streamlit Community Cloud est gratuit
  - Limite : 1 app publique par compte GitHub
  - Pour plus d'apps, utilisez Streamlit Cloud for Teams (payant)

## ✅ Checklist Finale

Avant de déployer, vérifiez :

- [ ] Tous les fichiers sont présents
- [ ] `requirements.txt` est complet
- [ ] `.gitignore` est créé
- [ ] L'application fonctionne localement (`streamlit run app.py`)
- [ ] Tous les modèles sont dans `models/`
- [ ] Le fichier principal s'appelle bien `app.py`

Bon déploiement ! 🚀

