# 🔧 Fix Version Scikit-learn

## Problème
Les modèles ont été sauvegardés avec scikit-learn 1.6.1, mais Render installe automatiquement la version 1.8.0, causant des warnings de compatibilité.

## Solution
Fixer scikit-learn à la version 1.6.1 dans `requirements.txt` pour correspondre à la version utilisée lors de la sauvegarde des modèles.

## Changement effectué

```txt
scikit-learn==1.6.1  # Au lieu de scikit-learn>=1.5.0
```

## Pourquoi cette version ?

- Les modèles ont été sauvegardés avec scikit-learn 1.6.1
- Utiliser une version différente peut causer :
  - Des warnings de compatibilité
  - Des erreurs lors du chargement
  - Des résultats incorrects

## Après le déploiement

Les warnings devraient disparaître et les modèles se chargeront correctement.

## Note

Si vous ré-entraînez les modèles avec une nouvelle version de scikit-learn, mettez à jour `requirements.txt` en conséquence.

