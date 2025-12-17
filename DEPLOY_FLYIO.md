# Guide de déploiement sur Fly.io

## ✈️ Déploiement sur Fly.io

Fly.io est une plateforme performante avec un plan gratuit généreux.

### Étapes de déploiement :

1. **Installer Fly CLI**
   ```bash
   # Windows (PowerShell)
   powershell -Command "iwr https://fly.io/install.ps1 -useb | iex"
   
   # Ou téléchargez depuis https://fly.io/docs/getting-started/installing-flyctl/
   ```

2. **Créer un compte**
   ```bash
   fly auth signup
   ```

3. **Créer un fichier `fly.toml`** (déjà créé ci-dessous)

4. **Déployer**
   ```bash
   fly launch
   ```
   - Suivez les instructions
   - Fly.io détectera automatiquement votre app Python

5. **URL de votre app**
   - Fly.io générera une URL comme : `https://sante-plus-app.fly.dev`

### Avantages de Fly.io :
- ✅ Plan gratuit généreux (3 VMs gratuites)
- ✅ Excellent support pour TensorFlow
- ✅ Performances élevées
- ✅ Déploiement via CLI (plus de contrôle)

