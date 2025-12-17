# 🩺 Santé Plus - Application de Diagnostic Assisté par ML

Application de diagnostic assisté par Machine Learning destinée à la **détection du cancer du sein**, basée sur le **Wisconsin Breast Cancer Diagnostic Dataset**.

## 🎯 Objectif

Aider à prédire si une tumeur est **✅ Bénigne** ou **⚠️ Maligne** à partir de caractéristiques morphologiques extraites d'images médicales.

## 🤖 Modèles Implémentés

L'application permet de tester et comparer **6 modèles** de Machine Learning :

1. **🧠 GRU-SVM** - Modèle hybride combinant un réseau récurrent (GRU) et un SVM
2. **📈 Linear Regression** - Régression linéaire utilisée comme classifieur
3. **🧩 MLP** - Réseau de neurones artificiels multicouches
4. **📍 k-NN** - Classification basée sur la distance entre observations
5. **🔁 Softmax Regression** - Régression logistique multiclasses
6. **📦 SVM** - Classifieur à marge maximale

## 🚀 Installation Locale

### Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### Installation

1. **Cloner le repository** :
```bash
git clone https://github.com/VOTRE_USERNAME/sante-plus-app.git
cd sante-plus-app
```

2. **Créer un environnement virtuel** (recommandé) :
```bash
python -m venv venv
# Sur Windows
venv\Scripts\activate
# Sur Mac/Linux
source venv/bin/activate
```

3. **Installer les dépendances** :
```bash
pip install -r requirements.txt
```

4. **Lancer l'application** :
```bash
streamlit run app.py
```

L'application s'ouvrira automatiquement dans votre navigateur à l'adresse `http://localhost:8501`

## 📊 Dataset

- **Dataset** : Wisconsin Breast Cancer Diagnostic Dataset (WDBC)
- **Observations** : 569
- **Caractéristiques** : 22 (après sélection de features)
- **Type** : Classification binaire (Bénin / Malin)

## 📁 Structure du Projet

```
sante_plus_app/
├── app.py                 # Fichier principal Streamlit
├── style.css             # Styles CSS personnalisés
├── requirements.txt      # Dépendances Python
├── README.md            # Ce fichier
├── DEPLOYMENT.md        # Guide de déploiement
├── pages/               # Pages de l'application
│   ├── 01_Accueil.py
│   ├── 02_Modele_1_GRU_SVM.py
│   ├── 03_Modele_2_Linear_Regression.py
│   ├── 04_Modele_3_MLP.py
│   ├── 05_Modele_4_Softmax.py
│   ├── 07_Model_5_SVM.py
│   ├── 07_Modele_6_knn.py
│   ├── 08_A_Propos.py
│   └── 09_Comparaison_Modeles.py
├── models/              # Modèles ML entraînés (.pkl)
│   ├── gru_svm.pkl
│   ├── knn.pkl
│   ├── linear_regression.pkl
│   ├── MLP.pkl
│   ├── scaler.pkl
│   ├── softmax.pkl
│   └── svm.pkl
└── data/                # Données
    └── data.csv
```

## 🛠️ Technologies Utilisées

- **Python** - Langage de programmation
- **Streamlit** - Framework web pour l'interface
- **Scikit-learn** - Bibliothèque ML
- **TensorFlow/Keras** - Deep Learning
- **Pandas** - Manipulation de données
- **NumPy** - Calculs numériques
- **Matplotlib/Seaborn** - Visualisations

## ⚠️ Avertissement Médical

**Cette application est un outil d'aide à la décision et ne remplace pas un diagnostic médical professionnel.**

Les résultats fournis par les modèles de Machine Learning sont à titre informatif uniquement. Consultez toujours un professionnel de santé pour un diagnostic complet et approprié.

## 📝 Licence

Ce projet est réalisé dans le cadre d'un module académique de Machine Learning / Data Mining.

## 👨‍💻 Auteur

Projet réalisé dans le cadre d'un module de Machine Learning / Data Mining, suivant la méthodologie **CRISP-DM**.

## 🔗 Déploiement

Pour déployer l'application sur Streamlit Cloud, consultez le fichier [DEPLOYMENT.md](DEPLOYMENT.md).

---

**Santé Plus** 💙 - Application de diagnostic assisté par Machine Learning

