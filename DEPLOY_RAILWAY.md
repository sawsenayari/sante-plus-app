# Guide de déploiement sur Railway

## 🚂 Déploiement sur Railway

Railway est une excellente plateforme qui gère très bien les dépendances lourdes comme TensorFlow.

### Étapes de déploiement :

1. **Créer un compte sur Railway**
   - Allez sur https://railway.app
   - Créez un compte gratuit (avec GitHub)
   - Vous recevrez $5 de crédits gratuits par mois

2. **Créer un nouveau projet**
   - Cliquez sur "New Project"
   - Sélectionnez "Deploy from GitHub repo"
   - Choisissez votre repository `sante-plus-app`

3. **Configuration automatique**
   - Railway détectera automatiquement que c'est une app Python
   - Il utilisera `requirements.txt` pour installer les dépendances

4. **Ajouter les variables d'environnement** (optionnel)
   - Dans "Variables", ajoutez :
     - `TF_CPP_MIN_LOG_LEVEL` = `3`

5. **Configurer le service**
   - Railway créera automatiquement un service web
   - Le port sera automatiquement configuré
   - Vous devrez peut-être ajouter une variable :
     - `PORT` = sera automatiquement défini par Railway

6. **Modifier le start command** (si nécessaire)
   - Dans les settings du service, ajoutez :
   - **Start Command** : `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`

7. **Déployer**
   - Railway déploiera automatiquement
   - Attendez 5-10 minutes pour le premier déploiement

8. **URL de votre app**
   - Railway générera une URL comme : `https://sante-plus-app.up.railway.app`

### Avantages de Railway :
- ✅ $5 de crédits gratuits par mois (suffisant pour un projet étudiant)
- ✅ Excellent support pour TensorFlow
- ✅ Déploiement automatique depuis GitHub
- ✅ Pas de limite d'inactivité
- ✅ Interface moderne et intuitive

### Note importante :
- Avec $5 de crédits, vous pouvez faire tourner une app Streamlit 24/7 pendant environ 2-3 semaines
- Ou utiliser l'app de manière intermittente pendant tout le mois

