import streamlit as st
from streamlit_option_menu import option_menu

# Configuration de la page
st.set_page_config(
    page_title="Accueil - Santé Plus",
    page_icon="❤️",
    layout="wide"
)

# Message d'avertissement pour les erreurs 502 (plan gratuit Render)
if 'show_502_warning' not in st.session_state:
    st.session_state.show_502_warning = True

if st.session_state.show_502_warning:
    st.warning("""
    ⚠️ **Erreur 502 ?** 
    
    Sur le plan gratuit de Render, l'application se met en veille après 15 minutes d'inactivité.
    
    **Solution immédiate :**
    1. Attendez 30-60 secondes
    2. Rafraîchissez la page (F5 ou Ctrl+R)
    3. L'application redémarrera automatiquement
    
    **Solution définitive :** Utilisez un service de keep-alive gratuit comme UptimeRobot pour empêcher la mise en veille.
    """)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Ne plus afficher"):
            st.session_state.show_502_warning = False
            st.rerun()
    with col2:
        if st.button("📖 Guide complet"):
            st.info("""
            **Guide pour éviter les erreurs 502 :**
            
            1. **UptimeRobot (Gratuit)** : https://uptimerobot.com
               - Créez un compte gratuit
               - Ajoutez un monitor HTTP(s)
               - URL : Votre URL Render
               - Interval : 5 minutes
               - Cela ping votre app toutes les 5 minutes
            
            2. **Alternative : Render Paid Plan**
               - $7/mois pour le plan Starter
               - L'app reste toujours active
               - Pas de délai de démarrage
            """)

# Chargement du CSS
def load_css():
    try:
        with open("style.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except:
        pass

load_css()

# =========================
# En-tête avec design moderne
# =========================
st.markdown("""
<div class="fade-in">
    <h1 style="text-align: center; color: #1f77b4; margin-bottom: 0.5rem;">
        🩺 Santé Plus
    </h1>
    <p style="text-align: center; font-size: 1.2rem; color: #6c757d; margin-bottom: 2rem;">
        Application de diagnostic assisté par Machine Learning
    </p>
</div>
""", unsafe_allow_html=True)

# =========================
# Description principale
# =========================
st.markdown("""
<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            padding: 2rem; border-radius: 15px; color: white; margin-bottom: 2rem;">
    <h2 style="color: white; margin-bottom: 1rem;">🎯 Objectif</h2>
    <p style="font-size: 1.1rem; line-height: 1.8;">
        Santé Plus est une application de diagnostic assisté destinée à la <strong>détection du cancer du sein</strong>, 
        basée sur le <strong>Wisconsin Breast Cancer Diagnostic Dataset</strong>.
    </p>
    <p style="font-size: 1.1rem; line-height: 1.8; margin-top: 1rem;">
        L'objectif principal est d'aider à prédire si une tumeur est <strong>✅ Bénigne</strong> ou <strong>⚠️ Maligne</strong> 
        à partir de caractéristiques morphologiques extraites d'images médicales.
    </p>
</div>
""", unsafe_allow_html=True)

# =========================
# Section Comparaison
# =========================
st.markdown("### 📊 Comparaison des Modèles")

col_comp1, col_comp2 = st.columns([2, 1])

with col_comp1:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #9467bd 0%, #c5b0d5 100%); 
                padding: 1.5rem; border-radius: 12px; color: white; margin-bottom: 2rem;">
        <h3 style="color: white; margin-bottom: 0.5rem;">🔍 Comparez tous les modèles en une seule fois</h3>
        <p style="font-size: 1rem; line-height: 1.6; margin: 0;">
            Utilisez la page de comparaison pour tester tous les modèles avec les mêmes caractéristiques 
            et voir leurs prédictions côte à côte. Analysez le consensus et les différences entre les algorithmes.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col_comp2:
    if st.button("📊 Accéder à la Comparaison", use_container_width=True, type="primary"):
        st.switch_page("pages/09_Comparaison_Modeles.py")

st.markdown("---")

# =========================
# Cartes des modèles disponibles
# =========================
st.markdown("### 🤖 Modèles de Machine Learning disponibles")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card fade-in" style="cursor: pointer;" onclick="window.location.href='?page=02_Modele_1_GRU_SVM'">
        <h3 style="color: #1f77b4; margin-bottom: 0.5rem;">🧠 GRU-SVM</h3>
        <p style="color: #6c757d; margin-bottom: 1rem;">
            Modèle hybride combinant un réseau récurrent (GRU) et un SVM pour une classification avancée.
        </p>
        <span class="badge badge-primary">Modèle Hybride</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card fade-in" style="cursor: pointer;" onclick="window.location.href='?page=04_Modele_3_MLP'">
        <h3 style="color: #1f77b4; margin-bottom: 0.5rem;">🧩 MLP</h3>
        <p style="color: #6c757d; margin-bottom: 1rem;">
            Réseau de neurones artificiels multicouches entraîné pour la classification.
        </p>
        <span class="badge badge-primary">Deep Learning</span>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card fade-in" style="cursor: pointer;" onclick="window.location.href='?page=03_Modele_2_Linear_Regression'">
        <h3 style="color: #1f77b4; margin-bottom: 0.5rem;">📈 Linear Regression</h3>
        <p style="color: #6c757d; margin-bottom: 1rem;">
            Régression linéaire utilisée comme classifieur via un seuil de décision.
        </p>
        <span class="badge badge-primary">Régression</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card fade-in" style="cursor: pointer;" onclick="window.location.href='?page=07_Modele_6_knn'">
        <h3 style="color: #1f77b4; margin-bottom: 0.5rem;">📍 k-NN</h3>
        <p style="color: #6c757d; margin-bottom: 1rem;">
            Classification basée sur la distance entre observations (k-Nearest Neighbors).
        </p>
        <span class="badge badge-primary">Instance-Based</span>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card fade-in" style="cursor: pointer;" onclick="window.location.href='?page=05_Modele_4_Softmax'">
        <h3 style="color: #1f77b4; margin-bottom: 0.5rem;">🔁 Softmax Regression</h3>
        <p style="color: #6c757d; margin-bottom: 1rem;">
            Régression logistique multiclasses (Softmax) pour la classification probabiliste.
        </p>
        <span class="badge badge-primary">Probabiliste</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card fade-in" style="cursor: pointer;" onclick="window.location.href='?page=07_Model_5_SVM'">
        <h3 style="color: #1f77b4; margin-bottom: 0.5rem;">📦 SVM</h3>
        <p style="color: #6c757d; margin-bottom: 1rem;">
            Classifieur à marge maximale avec régularisation L2.
        </p>
        <span class="badge badge-primary">SVM</span>
    </div>
    """, unsafe_allow_html=True)

# =========================
# Instructions d'utilisation
# =========================
st.markdown("---")
st.markdown("### 📋 Comment utiliser l'application ?")

col_info1, col_info2 = st.columns(2)

with col_info1:
    st.markdown("""
    <div style="background-color: #e7f3ff; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #1f77b4;">
        <h4 style="color: #1f77b4; margin-bottom: 1rem;">1️⃣ Sélectionnez un modèle</h4>
        <p style="color: #212529;">
            Choisissez l'un des 6 modèles disponibles dans la barre de navigation ou cliquez sur les cartes ci-dessus.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col_info2:
    st.markdown("""
    <div style="background-color: #fff4e6; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #ff7f0e;">
        <h4 style="color: #ff7f0e; margin-bottom: 1rem;">2️⃣ Entrez les caractéristiques</h4>
        <p style="color: #212529;">
            Remplissez le formulaire avec les 22 caractéristiques morphologiques de la tumeur.
        </p>
    </div>
    """, unsafe_allow_html=True)

col_info3, col_info4 = st.columns(2)

with col_info3:
    st.markdown("""
    <div style="background-color: #e8f5e9; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #2ca02c;">
        <h4 style="color: #2ca02c; margin-bottom: 1rem;">3️⃣ Obtenez la prédiction</h4>
        <p style="color: #212529;">
            Cliquez sur "Prédire" pour obtenir le diagnostic : Bénigne ✅ ou Maligne ⚠️
        </p>
    </div>
    """, unsafe_allow_html=True)

with col_info4:
    st.markdown("""
    <div style="background-color: #fce4ec; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #d62728;">
        <h4 style="color: #d62728; margin-bottom: 1rem;">4️⃣ Comparez les modèles</h4>
        <p style="color: #212529;">
            Testez différents modèles avec les mêmes données pour comparer leurs performances.
        </p>
    </div>
    """, unsafe_allow_html=True)

# =========================
# Informations sur le dataset
# =========================
st.markdown("---")
st.markdown("### 📊 À propos du dataset")

st.markdown("""
<div style="background-color: #f8f9fa; padding: 1.5rem; border-radius: 10px;">
    <p style="font-size: 1rem; line-height: 1.8; color: #212529;">
        <strong>Wisconsin Breast Cancer Diagnostic Dataset (WDBC)</strong><br>
        • <strong>569 observations</strong> de tumeurs mammaires<br>
        • <strong>22 caractéristiques</strong> morphologiques sélectionnées<br>
        • Classification binaire : <strong>Bénigne</strong> (357 cas) / <strong>Maligne</strong> (212 cas)
    </p>
</div>
""", unsafe_allow_html=True)

# =========================
# Lien vers À Propos
# =========================
st.markdown("---")
col_about, _ = st.columns([1, 3])
with col_about:
    if st.button("ℹ️ En savoir plus", use_container_width=True):
        st.switch_page("pages/08_A_Propos.py")
