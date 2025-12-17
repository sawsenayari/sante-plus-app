# 🐳 Déploiement avec Docker sur Render

## Pourquoi Docker ?

Docker garantit Python 3.11 et évite les problèmes de compatibilité avec Python 3.13.

## Étapes de déploiement

### 1. Créer un nouveau service sur Render

1. Allez sur https://dashboard.render.com
2. Cliquez sur **"New"** → **"Web Service"**
3. Connectez votre repository GitHub `sante-plus-app`

### 2. Configuration Docker

1. **Environment** : Sélectionnez **"Docker"** (pas Python)
2. **Name** : `sante-plus-app`
3. **Region** : Choisissez votre région
4. **Branch** : `main`
5. **Root Directory** : Laissez vide (ou `/`)

### 3. Build & Deploy

Render détectera automatiquement le `Dockerfile` et :
- Utilisera Python 3.11 (défini dans Dockerfile)
- Installera toutes les dépendances
- Exposera le port 8080

### 4. Variables d'environnement (optionnel)

Dans **Environment Variables** :
- `TF_CPP_MIN_LOG_LEVEL` = `3`

### 5. Créer le service

- Cliquez sur **"Create Web Service"**
- Render va automatiquement build l'image Docker
- Attendez 5-10 minutes pour le premier build

## ✅ Avantages

- ✅ Python 3.11 garanti
- ✅ Pas de problème de compatibilité
- ✅ Environnement reproductible
- ✅ Build plus rapide (pas de compilation numpy)

## 🔍 Vérification

Après le déploiement, vérifiez les logs :
- Vous devriez voir : `FROM python:3.11-slim`
- Plus d'erreur `numpy==2.0.0rc1`
- Build réussi

## 📝 Note

Le `Dockerfile` est déjà configuré avec :
- Python 3.11
- Toutes les dépendances
- Port 8080
- Commande de démarrage Streamlit

