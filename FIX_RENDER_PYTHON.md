# 🔧 Fix : Problème Python 3.13 sur Render

## Problème
Render utilise Python 3.13 par défaut, ce qui cause des erreurs avec numpy et scikit-learn.

## Solution : Forcer Python 3.11

### Option 1 : Via l'interface Render (RECOMMANDÉ)

1. **Dans votre service Render**, allez dans "Settings"
2. **Trouvez la section "Environment"**
3. **Ajoutez une variable d'environnement** :
   - **Key** : `PYTHON_VERSION`
   - **Value** : `3.11.14`
4. **Sauvegardez** et **redéployez**

### Option 2 : Via render.yaml (déjà configuré)

Le fichier `render.yaml` est déjà configuré avec Python 3.11.14.

**IMPORTANT** : Si vous utilisez `render.yaml`, assurez-vous que :
- Le fichier est à la racine de votre projet
- Render détecte automatiquement le fichier
- Sinon, utilisez l'Option 1 ci-dessus

### Option 3 : Modifier le Build Command

Dans les settings de votre service Render :

**Build Command** :
```bash
pip install --upgrade pip setuptools wheel && pip install -r requirements.txt
```

**Start Command** :
```bash
streamlit run app.py --server.port $PORT --server.address 0.0.0.0
```

## 📝 Étapes détaillées dans Render

1. Allez sur https://dashboard.render.com
2. Cliquez sur votre service `sante-plus-app`
3. Cliquez sur "Environment" dans le menu de gauche
4. Cliquez sur "Add Environment Variable"
5. Ajoutez :
   - **Key** : `PYTHON_VERSION`
   - **Value** : `3.11.14`
6. Cliquez sur "Save Changes"
7. Allez dans "Manual Deploy" → "Deploy latest commit"

## ✅ Vérification

Après le redéploiement, vérifiez les logs :
- Vous devriez voir : `Using Python 3.11.14`
- Plus d'erreur `numpy==2.0.0rc1`
- Le build devrait réussir

## 🚨 Si le problème persiste

1. **Supprimez le service** dans Render
2. **Recréez-le** en suivant ces étapes :
   - New → Web Service
   - Connectez votre repo
   - **AVANT de créer**, dans "Advanced" :
     - Ajoutez la variable `PYTHON_VERSION` = `3.11.14`
   - Puis créez le service

