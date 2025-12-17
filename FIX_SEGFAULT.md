# 🔧 Fix Segmentation Fault (Status 139)

## Problème
L'application crash avec le statut 139 (Segmentation Fault), généralement causé par TensorFlow.

## Solutions implémentées

### 1. Variables d'environnement dans Dockerfile
- `TF_ENABLE_ONEDNN_OPTS=0` : Désactive OneDNN
- `TF_DISABLE_MKL=1` : Désactive MKL
- `OMP_NUM_THREADS=1` : Limite les threads OpenMP
- `MKL_NUM_THREADS=1` : Limite les threads MKL

### 2. Utilitaire de chargement sécurisé
- Fichier `utils/tf_safe_loader.py` créé
- Charge TensorFlow avec gestion d'erreurs
- Configure les threads pour éviter les segfaults

### 3. Configuration TensorFlow
- Limite les threads inter-op et intra-op à 1
- Active le soft device placement
- Désactive les optimisations problématiques

## Vérification

Après le déploiement, vérifiez les logs :
- Plus d'erreur "Exited with status 139"
- L'app démarre correctement
- Les modèles TensorFlow se chargent sans crash

## Si le problème persiste

1. **Vérifier les logs Render** pour voir où exactement le crash se produit
2. **Réduire encore plus les ressources** utilisées par TensorFlow
3. **Considérer d'utiliser TensorFlow Lite** pour les modèles
4. **Upgrade Render** vers un plan avec plus de mémoire

## Notes

- Le statut 139 = Segmentation Fault (SIGSEGV)
- Souvent causé par TensorFlow qui accède à de la mémoire invalide
- Les variables d'environnement limitent l'utilisation de la mémoire/threads

