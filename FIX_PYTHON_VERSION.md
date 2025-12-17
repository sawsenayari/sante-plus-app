# 🔧 Solution : Configurer Python 3.11 dans Streamlit Cloud

## Problème
TensorFlow n'est pas compatible avec Python 3.13 (utilisé par défaut par Streamlit Cloud).

## Solution : Configurer Python 3.11 dans Streamlit Cloud

### Option 1 : Via l'interface Streamlit Cloud (Recommandé)

1. **Allez sur https://share.streamlit.io/**
2. **Connectez-vous** et ouvrez votre application `sante-plus-app`
3. **Cliquez sur "⋮" (trois points)** en haut à droite
4. **Sélectionnez "Settings"**
5. **Dans la section "Python version"**, sélectionnez **Python 3.11**
6. **Sauvegardez** les changements
7. **Redéployez** l'application (cliquez sur "Reboot app")

### Option 2 : Vérifier que runtime.txt est correct

Le fichier `runtime.txt` doit contenir exactement :
```
python-3.11
```

Assurez-vous que ce fichier est bien dans la racine de votre projet et qu'il est commité sur GitHub.

### Option 3 : Si Python 3.11 n'est pas disponible

Si Python 3.11 n'est pas disponible dans les options, essayez :

1. **Supprimez temporairement TensorFlow** des requirements.txt
2. **Testez si l'app démarre** sans les modèles MLP/GRU-SVM
3. **Contactez le support Streamlit Cloud** pour demander Python 3.11

## Fichiers à vérifier

✅ `runtime.txt` doit contenir : `python-3.11`
✅ `requirements.txt` doit contenir : `tensorflow-cpu>=2.13.0,<2.16.0`

## Après la configuration

1. **Commitez et poussez** les changements :
```cmd
git add .
git commit -m "Fix: Configure Python 3.11 for TensorFlow compatibility"
git push
```

2. **Attendez le redéploiement** automatique (2-5 minutes)

3. **Vérifiez les logs** pour confirmer que Python 3.11 est utilisé

---

**Note** : Si Python 3.11 n'est toujours pas disponible, vous devrez peut-être attendre que Streamlit Cloud le supporte, ou utiliser une alternative à TensorFlow pour les modèles MLP/GRU-SVM.

