# 🚀 MLOps Simple - Guide de Déploiement

## 📋 Vue d'ensemble

Cette intégration MLOps simple comprend :
1. **Validation des modèles** avant déploiement
2. **CI/CD automatisé** avec GitHub Actions
3. **Déploiement automatique** sur Render

## 🔧 Structure

```
sante_plus_app/
├── scripts/
│   ├── validate_models.py    # Validation des modèles
│   └── check_deployment.py   # Vérification pré-déploiement
├── .github/workflows/
│   └── deploy.yml            # Pipeline CI/CD
└── models/                   # Modèles ML
```

## 🎯 Workflow MLOps

```
1. Développement
   └─> Modifier le code
   
2. Validation locale
   └─> python scripts/validate_models.py
   
3. Commit & Push
   └─> git add .
   └─> git commit -m "Update"
   └─> git push origin main
   
4. CI/CD automatique
   └─> GitHub Actions valide les modèles
   └─> Render déploie automatiquement
   
5. Vérification
   └─> Tester l'application déployée
```

## 📝 Utilisation

### 1. Validation locale

Avant de pousser votre code, validez les modèles :

```bash
python scripts/validate_models.py
```

Cela vérifie que :
- ✅ Tous les fichiers de modèles existent
- ✅ Les modèles peuvent être chargés
- ✅ Aucune erreur de corruption

### 2. Vérification pré-déploiement

Vérifiez que tout est prêt :

```bash
python scripts/check_deployment.py
```

### 3. Déploiement automatique

1. **Pousser vers GitHub** :
   ```bash
   git add .
   git commit -m "Update models"
   git push origin main
   ```

2. **GitHub Actions** :
   - Valide automatiquement les modèles
   - Vérifie que tout est OK

3. **Render** :
   - Déploie automatiquement (si webhook configuré)
   - Ou déploiement manuel depuis le dashboard Render

## 🔄 Configuration GitHub Actions

Le workflow `.github/workflows/deploy.yml` :

- ✅ S'exécute sur chaque push vers `main`
- ✅ Valide les modèles avant déploiement
- ✅ Vérifie que tous les fichiers nécessaires existent

## 🚀 Configuration Render

### Option 1 : Déploiement automatique (Recommandé)

1. Dans Render, allez dans votre service
2. Settings → Build & Deploy
3. Activer "Auto-Deploy" : `Yes`
4. Branch : `main`

### Option 2 : Webhook GitHub

1. Dans Render, créez un webhook
2. URL : `https://api.render.com/v1/services/{service_id}/deploys`
3. Dans GitHub, ajoutez le webhook dans Settings → Webhooks

## 📊 Monitoring

### Vérifier les logs GitHub Actions

1. Allez sur votre repo GitHub
2. Onglet "Actions"
3. Voir les résultats du workflow

### Vérifier le déploiement Render

1. Dashboard Render
2. Voir les logs de build
3. Vérifier l'URL de l'application

## 🐛 Troubleshooting

### Erreur : "Modèles non trouvés"

```bash
# Vérifier que les modèles existent
ls -la models/

# Vérifier les chemins dans le code
python scripts/validate_models.py
```

### Erreur : "Validation échoue"

- Vérifier que tous les fichiers `.pkl` sont présents
- Vérifier qu'ils ne sont pas corrompus
- Ré-entraîner les modèles si nécessaire

### Déploiement ne se déclenche pas

1. Vérifier que le push est sur `main`
2. Vérifier les logs GitHub Actions
3. Vérifier la configuration Render

## ✅ Checklist avant déploiement

- [ ] Tous les modèles sont validés localement
- [ ] `requirements.txt` est à jour
- [ ] `Dockerfile` est correct
- [ ] `render.yaml` est configuré
- [ ] Tests locaux passent
- [ ] Code poussé vers `main`

## 📚 Commandes utiles

```bash
# Validation
python scripts/validate_models.py

# Vérification complète
python scripts/check_deployment.py

# Test local
streamlit run app.py

# Build Docker local
docker build -t sante-plus .
docker run -p 8501:8501 sante-plus
```

## 🎉 Avantages de cette approche

- ✅ **Simple** : Pas de complexité inutile
- ✅ **Automatique** : Déploiement sans intervention
- ✅ **Sûr** : Validation avant déploiement
- ✅ **Rapide** : Pipeline léger et efficace

