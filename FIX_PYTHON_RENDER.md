# 🔧 Fix Python 3.13 → 3.11 sur Render

## Problème
Render utilise Python 3.13.4 par défaut, ce qui cause des erreurs avec scikit-learn et numpy.

## Solution : Forcer Python 3.11 dans Render

### Méthode 1 : Via l'interface Render (RECOMMANDÉ)

1. **Allez sur votre service Render**
   - Dashboard Render → Votre service `sante-plus-app`

2. **Settings → Environment**
   - Trouvez la section "Python Version"
   - Changez de `3.13.4` (ou default) à `3.11.14`
   - OU ajoutez une variable d'environnement :
     - **Key** : `PYTHON_VERSION`
     - **Value** : `3.11.14`

3. **Settings → Build & Deploy**
   - Vérifiez que le Build Command est :
     ```
     pip install --upgrade pip setuptools wheel && pip install -r requirements.txt
     ```

4. **Sauvegarder et redéployer**
   - Cliquez sur "Save Changes"
   - Allez dans "Manual Deploy" → "Deploy latest commit"

### Méthode 2 : Via render.yaml (déjà configuré)

Le fichier `render.yaml` contient maintenant :
```yaml
pythonVersion: 3.11.14
```

**IMPORTANT** : Si Render ne détecte pas automatiquement `render.yaml`, utilisez la Méthode 1.

### Méthode 3 : Via runtime.txt (déjà configuré)

Le fichier `runtime.txt` contient :
```
python-3.11.14
```

## ✅ Vérification

Après le redéploiement, vérifiez les logs :
- Vous devriez voir : `Installing Python version 3.11.14...`
- Plus d'erreur `numpy==2.0.0rc1`
- Le build devrait réussir

## 🚨 Si le problème persiste

1. **Supprimez le service** dans Render
2. **Recréez-le** en suivant ces étapes :
   - New → Web Service
   - Connectez votre repo
   - **AVANT de créer**, dans "Advanced" :
     - Python Version : `3.11.14`
     - OU ajoutez `PYTHON_VERSION` = `3.11.14` dans Environment Variables
   - Puis créez le service

