import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="À propos - Santé Plus",
    page_icon="ℹ️",
    layout="wide"
)

# Chargement du CSS
def load_css():
    try:
        with open("style.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except:
        pass

load_css()

# =========================
# Bouton de retour
# =========================
col_back, col_title = st.columns([1, 5])
with col_back:
    if st.button("← Retour", use_container_width=True):
        st.switch_page("pages/01_Accueil.py")

with col_title:
    st.markdown("""
    <div style="margin-top: 0.5rem;">
        <h1 style="color: #1f77b4; margin-bottom: 0.5rem;">ℹ️ À propos du projet Santé Plus</h1>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# =========================
# Présentation générale
# =========================
st.markdown("""
<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            padding: 2rem; border-radius: 15px; color: white; margin-bottom: 2rem;">
    <h2 style="color: white; margin-bottom: 1rem;">🩺 Présentation générale</h2>
    <p style="font-size: 1.05rem; line-height: 1.8;">
        <strong>Santé Plus</strong> est une application de <em>diagnostic assisté par Machine Learning</em>  
        destinée à la <strong>détection du cancer du sein</strong>, basée sur le  
        <strong>Wisconsin Breast Cancer Diagnostic Dataset</strong>.
    </p>
    <p style="font-size: 1.05rem; line-height: 1.8; margin-top: 1rem;">
        L'objectif principal est d'aider à prédire si une tumeur est :
    </p>
    <ul style="font-size: 1.05rem; line-height: 1.8;">
        <li>✅ <strong>Bénigne</strong></li>
        <li>⚠️ <strong>Maligne</strong></li>
    </ul>
    <p style="font-size: 1.05rem; line-height: 1.8; margin-top: 1rem;">
        à partir de <strong>caractéristiques morphologiques extraites d'images médicales</strong>.
    </p>
</div>
""", unsafe_allow_html=True)

# =========================
# Objectifs du projet
# =========================
st.markdown("### 🎯 Objectifs du projet")

col_obj1, col_obj2 = st.columns(2)

with col_obj1:
    st.markdown("""
    <div class="card">
        <h4 style="color: #1f77b4;">📊 Pipeline complet</h4>
        <p>Mise en œuvre d'un pipeline complet de Data Mining suivant la méthodologie CRISP-DM.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <h4 style="color: #1f77b4;">🔬 Évaluation des performances</h4>
        <p>Évaluation des modèles à l'aide de métriques adaptées au contexte médical (Accuracy, Sensibilité, Spécificité, AUC-ROC).</p>
    </div>
    """, unsafe_allow_html=True)

with col_obj2:
    st.markdown("""
    <div class="card">
        <h4 style="color: #1f77b4;">🤖 Comparaison d'algorithmes</h4>
        <p>Comparaison de plusieurs algorithmes de Machine Learning sur le même dataset.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <h4 style="color: #1f77b4;">💻 Interface interactive</h4>
        <p>Proposer une interface interactive et user-friendly pour tester les modèles en temps réel.</p>
    </div>
    """, unsafe_allow_html=True)

# =========================
# Données utilisées
# =========================
st.markdown("### 🔬 Données utilisées")

st.markdown("""
<div style="background-color: #f8f9fa; padding: 1.5rem; border-radius: 12px; border-left: 5px solid #1f77b4;">
    <ul style="font-size: 1rem; line-height: 2; color: #212529;">
        <li><strong>Dataset</strong> : Wisconsin Breast Cancer Diagnostic</li>
        <li><strong>Nombre d'observations</strong> : 569</li>
        <li><strong>Nombre de variables</strong> : 30 (réduites à 22 après sélection de features)</li>
        <li><strong>Type de problème</strong> : Classification binaire (Bénin / Malin)</li>
    </ul>
    <p style="margin-top: 1rem; color: #6c757d;">
        Les variables décrivent notamment : la taille du noyau cellulaire, la texture, 
        la concavité, l'irrégularité des contours.
    </p>
</div>
""", unsafe_allow_html=True)

# =========================
# Modèles implémentés
# =========================
st.markdown("### 🤖 Modèles implémentés")

st.markdown("L'application permet de tester et comparer **6 modèles** :")

models_data = [
    ("🧠 GRU-SVM", "Modèle hybride combinant un réseau récurrent (GRU) et un SVM", "#667eea"),
    ("📈 Régression Linéaire", "Utilisée comme classifieur via un seuil de décision", "#ff7f0e"),
    ("🧩 Multilayer Perceptron (MLP)", "Réseau de neurones artificiels multicouches", "#2ca02c"),
    ("📍 k-Nearest Neighbors (k-NN)", "Classification basée sur la distance entre observations", "#8c564b"),
    ("🔁 Softmax Regression", "Variante de la régression logistique", "#9467bd"),
    ("📦 Support Vector Machine (SVM)", "Classifieur à marge maximale avec régularisation L2", "#d62728")
]

for i in range(0, len(models_data), 2):
    col_mod1, col_mod2 = st.columns(2)
    with col_mod1:
        icon, desc, color = models_data[i]
        st.markdown(f"""
        <div class="card" style="border-left: 5px solid {color};">
            <h4 style="color: {color}; margin-bottom: 0.5rem;">{icon}</h4>
            <p style="color: #6c757d;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)
    if i + 1 < len(models_data):
        with col_mod2:
            icon, desc, color = models_data[i + 1]
            st.markdown(f"""
            <div class="card" style="border-left: 5px solid {color};">
                <h4 style="color: {color}; margin-bottom: 0.5rem;">{icon}</h4>
                <p style="color: #6c757d;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)

# =========================
# Métriques d'évaluation
# =========================
st.markdown("### 📊 Métriques d'évaluation")

st.markdown("""
<div style="background-color: #e7f3ff; padding: 1.5rem; border-radius: 12px; border-left: 5px solid #1f77b4;">
    <p style="font-size: 1rem; line-height: 1.8; color: #212529; margin-bottom: 1rem;">
        Les modèles sont évalués à l'aide de :
    </p>
    <ul style="font-size: 1rem; line-height: 2; color: #212529;">
        <li><strong>Accuracy</strong> : Précision globale du modèle</li>
        <li><strong>Sensibilité (TPR)</strong> : Capacité à détecter les tumeurs malignes</li>
        <li><strong>Spécificité (TNR)</strong> : Capacité à identifier les tumeurs bénignes</li>
        <li><strong>AUC-ROC</strong> : Capacité de discrimination globale</li>
    </ul>
    <p style="margin-top: 1rem; color: #212529; font-weight: 600;">
        👉 Une attention particulière est portée à la <strong>sensibilité</strong>, 
        critique dans un contexte médical (éviter les faux négatifs).
    </p>
</div>
""", unsafe_allow_html=True)

# =========================
# Choix méthodologiques
# =========================
st.markdown("### 🧠 Choix méthodologiques")

st.markdown("""
<div style="background-color: #fff4e6; padding: 1.5rem; border-radius: 12px; border-left: 5px solid #ff7f0e;">
    <ul style="font-size: 1rem; line-height: 2; color: #212529;">
        <li><strong>Standardisation des données</strong> (StandardScaler)</li>
        <li><strong>Sélection de features</strong> pour réduire la redondance</li>
        <li><strong>Comparaison avec et sans PCA</strong></li>
        <li><strong>Même scaler utilisé pour tous les modèles</strong></li>
        <li><strong>Déploiement interactif avec Streamlit</strong></li>
    </ul>
</div>
""", unsafe_allow_html=True)

# =========================
# Déploiement
# =========================
st.markdown("### 🚀 Déploiement")

st.markdown("""
<div style="background-color: #e8f5e9; padding: 1.5rem; border-radius: 12px; border-left: 5px solid #2ca02c;">
    <p style="font-size: 1rem; line-height: 1.8; color: #212529; margin-bottom: 1rem;">
        L'application est développée avec :
    </p>
    <ul style="font-size: 1rem; line-height: 2; color: #212529;">
        <li><strong>Python</strong></li>
        <li><strong>Scikit-learn</strong></li>
        <li><strong>TensorFlow / Keras</strong></li>
        <li><strong>Streamlit</strong></li>
    </ul>
    <p style="margin-top: 1rem; color: #212529;">
        Elle permet : la saisie manuelle des caractéristiques, l'exécution des modèles entraînés, 
        et l'affichage du diagnostic prédit en temps réel.
    </p>
</div>
""", unsafe_allow_html=True)

# =========================
# Conclusion
# =========================
st.markdown("### 📌 Conclusion")

st.markdown("""
<div style="background: linear-gradient(135deg, #84fab0 0%, #8fd3f4 100%); 
            padding: 2rem; border-radius: 15px; margin: 2rem 0;">
    <p style="font-size: 1.05rem; line-height: 1.8; color: #212529;">
        Ce projet illustre comment le <strong>Machine Learning</strong> peut être utilisé comme
        <strong>outil d'aide à la décision médicale</strong>, tout en respectant les contraintes
        d'interprétabilité et d'évaluation propres au domaine de la santé.
    </p>
</div>
""", unsafe_allow_html=True)

# =========================
# Projet académique
# =========================
st.markdown("### 👩‍🎓 Projet académique")

st.markdown("""
<div style="background-color: #f8f9fa; padding: 1.5rem; border-radius: 12px;">
    <p style="font-size: 1rem; line-height: 1.8; color: #212529; margin-bottom: 1rem;">
        Projet réalisé dans le cadre d'un <strong>module de Machine Learning / Data Mining</strong>,  
        suivant la méthodologie <strong>CRISP-DM</strong> :
    </p>
    <ul style="font-size: 1rem; line-height: 2; color: #212529;">
        <li>Business Understanding</li>
        <li>Data Understanding</li>
        <li>Data Preparation</li>
        <li>Modeling</li>
        <li>Evaluation</li>
        <li>Deployment</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# =========================
# Message final
# =========================
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem;">
    <h3 style="color: #1f77b4;">Merci d'avoir consulté l'application Santé Plus 💙</h3>
    <p style="color: #6c757d; font-size: 1.1rem; margin-top: 1rem;">
        Cette application est un outil d'aide à la décision et ne remplace pas un diagnostic médical professionnel.
    </p>
</div>
""", unsafe_allow_html=True)
