# Guide de déploiement sur Render

## 🚀 Déploiement sur Render (Recommandé)

Render est une excellente alternative à Streamlit Cloud qui gère mieux TensorFlow.

### Étapes de déploiement :

1. **Créer un compte sur Render**
   - Allez sur https://render.com
   - Créez un compte gratuit (avec GitHub)

2. **Connecter votre repository GitHub**
   - Dans le dashboard Render, cliquez sur "New" → "Web Service"
   - Sélectionnez votre repository `sante-plus-app`
   - Render détectera automatiquement que c'est une app Streamlit

3. **Configuration**
   - **Name** : `sante-plus-app` (ou votre choix)
   - **Environment** : `Python 3`
   - **Build Command** : `pip install -r requirements.txt`
   - **Start Command** : `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`
   - **Python Version** : `3.11`

4. **Variables d'environnement** (optionnel)
   - `TF_CPP_MIN_LOG_LEVEL` = `3` (pour réduire les warnings TensorFlow)

5. **Déployer**
   - Cliquez sur "Create Web Service"
   - Render va automatiquement :
     - Cloner votre repo
     - Installer les dépendances
     - Démarrer votre app
   - Attendez 5-10 minutes pour le premier déploiement

6. **URL de votre app**
   - Render vous donnera une URL comme : `https://sante-plus-app.onrender.com`

### Avantages de Render :
- ✅ Gratuit (avec limite d'inactivité)
- ✅ Supporte bien TensorFlow
- ✅ Déploiement automatique depuis GitHub
- ✅ Pas de segfault avec TensorFlow
- ✅ Interface simple

### Note importante :
- L'app se met en veille après 15 minutes d'inactivité (plan gratuit)
- Le premier démarrage après veille peut prendre 30-60 secondes

