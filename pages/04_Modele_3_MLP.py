import streamlit as st
import numpy as np
import joblib
import os

# Désactiver les warnings TensorFlow
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# Importer Keras/TensorFlow avant de charger les modèles
try:
    import tensorflow as tf
    tf.get_logger().setLevel('ERROR')
    import keras
except ImportError:
    pass

# Configuration de la page
st.set_page_config(
    page_title="MLP - Santé Plus",
    page_icon="🧩",
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
        <h1 style="color: #1f77b4; margin-bottom: 0.5rem;">🧩 Multilayer Perceptron (MLP)</h1>
    </div>
    """, unsafe_allow_html=True)

# =========================
# Description du modèle
# =========================
st.markdown("""
<div style="background: linear-gradient(135deg, #2ca02c 0%, #98df8a 100%); 
            padding: 1.5rem; border-radius: 12px; color: white; margin-bottom: 2rem;">
    <p style="font-size: 1.05rem; line-height: 1.8; margin: 0;">
        Ce modèle est un réseau de neurones artificiels multicouches utilisé pour la classification 
        des tumeurs bénignes et malignes. Il apprend des patterns complexes dans les données.
    </p>
</div>
""", unsafe_allow_html=True)

# =========================
# Chargement modèle + scaler
# =========================
@st.cache_resource
def load_mlp():
    model = joblib.load("models/MLP.pkl")
    scaler = joblib.load("models/scaler.pkl")
    return model, scaler

mlp_model, scaler = load_mlp()

# =========================
# Formulaire des inputs
# =========================
st.markdown("### 🔢 Entrer les caractéristiques de la tumeur")
st.markdown("Remplissez les 22 caractéristiques morphologiques ci-dessous :")

with st.form("mlp_form"):
    st.markdown("#### Caractéristiques moyennes (Mean)")
    col1, col2, col3 = st.columns(3)

    with col1:
        radius_mean = st.number_input("Radius Mean", min_value=0.0, value=0.0, step=0.1, format="%.2f")
        texture_mean = st.number_input("Texture Mean", min_value=0.0, value=0.0, step=0.1, format="%.2f")
        area_mean = st.number_input("Area Mean", min_value=0.0, value=0.0, step=1.0, format="%.2f")
        smoothness_mean = st.number_input("Smoothness Mean", min_value=0.0, value=0.0, step=0.001, format="%.4f")

    with col2:
        compactness_mean = st.number_input("Compactness Mean", min_value=0.0, value=0.0, step=0.001, format="%.4f")
        concavity_mean = st.number_input("Concavity Mean", min_value=0.0, value=0.0, step=0.001, format="%.4f")
        concave_points_mean = st.number_input("Concave Points Mean", min_value=0.0, value=0.0, step=0.001, format="%.4f")
        symmetry_mean = st.number_input("Symmetry Mean", min_value=0.0, value=0.0, step=0.001, format="%.4f")

    with col3:
        fractal_dimension_mean = st.number_input("Fractal Dimension Mean", min_value=0.0, value=0.0, step=0.001, format="%.4f")
        radius_se = st.number_input("Radius SE", min_value=0.0, value=0.0, step=0.1, format="%.2f")
        area_se = st.number_input("Area SE", min_value=0.0, value=0.0, step=1.0, format="%.2f")
        compactness_se = st.number_input("Compactness SE", min_value=0.0, value=0.0, step=0.001, format="%.4f")

    st.markdown("#### Caractéristiques d'erreur standard (SE)")
    col4, col5, col6 = st.columns(3)

    with col4:
        concavity_se = st.number_input("Concavity SE", min_value=0.0, value=0.0, step=0.001, format="%.4f")
        concave_points_se = st.number_input("Concave Points SE", min_value=0.0, value=0.0, step=0.001, format="%.4f")

    st.markdown("#### Caractéristiques les plus défavorables (Worst)")
    col7, col8, col9 = st.columns(3)

    with col7:
        radius_worst = st.number_input("Radius Worst", min_value=0.0, value=0.0, step=0.1, format="%.2f")
        texture_worst = st.number_input("Texture Worst", min_value=0.0, value=0.0, step=0.1, format="%.2f")
        area_worst = st.number_input("Area Worst", min_value=0.0, value=0.0, step=1.0, format="%.2f")

    with col8:
        smoothness_worst = st.number_input("Smoothness Worst", min_value=0.0, value=0.0, step=0.001, format="%.4f")
        compactness_worst = st.number_input("Compactness Worst", min_value=0.0, value=0.0, step=0.001, format="%.4f")
        concavity_worst = st.number_input("Concavity Worst", min_value=0.0, value=0.0, step=0.001, format="%.4f")

    with col9:
        concave_points_worst = st.number_input("Concave Points Worst", min_value=0.0, value=0.0, step=0.001, format="%.4f")
        symmetry_worst = st.number_input("Symmetry Worst", min_value=0.0, value=0.0, step=0.001, format="%.4f")

    col_submit, _, _ = st.columns([1, 2, 2])
    with col_submit:
        submit = st.form_submit_button("🔍 Prédire", use_container_width=True, type="primary")

# =========================
# Prédiction
# =========================
if submit:
    X = np.array([[
        radius_mean, texture_mean, area_mean, smoothness_mean,
        compactness_mean, concavity_mean, concave_points_mean,
        symmetry_mean, fractal_dimension_mean,

        radius_se, area_se, compactness_se,
        concavity_se, concave_points_se,

        radius_worst, texture_worst, area_worst,
        smoothness_worst, compactness_worst,
        concavity_worst, concave_points_worst,
        symmetry_worst
    ]])

    # Standardisation
    X_scaled = scaler.transform(X)

    # Prédiction
    y_prob = mlp_model.predict(X_scaled)[0][0]
    y_pred = 1 if y_prob >= 0.5 else 0

    st.markdown("---")
    st.markdown("### 📊 Résultat de la prédiction")
    
    # Affichage de la probabilité
    st.metric("Probabilité de malignité", f"{y_prob:.4f}", f"Seuil: 0.5")
    
    if y_pred == 1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%); 
                    padding: 2rem; border-radius: 15px; text-align: center; margin: 2rem 0;">
            <h2 style="color: #d62728; margin-bottom: 1rem;">⚠️ Tumeur prédite comme MALIGNE</h2>
            <p style="font-size: 1.1rem; color: #212529;">
                Le modèle indique que cette tumeur présente des caractéristiques malignes.
                <br><strong>Consultez un professionnel de santé pour un diagnostic complet.</strong>
            </p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #84fab0 0%, #8fd3f4 100%); 
                    padding: 2rem; border-radius: 15px; text-align: center; margin: 2rem 0;">
            <h2 style="color: #2ca02c; margin-bottom: 1rem;">✅ Tumeur prédite comme BÉNIGNE</h2>
            <p style="font-size: 1.1rem; color: #212529;">
                Le modèle indique que cette tumeur présente des caractéristiques bénignes.
                <br><strong>Consultez un professionnel de santé pour un diagnostic complet.</strong>
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.info("⚠️ **Important** : Cette application est un outil d'aide à la décision et ne remplace pas un diagnostic médical professionnel.")
