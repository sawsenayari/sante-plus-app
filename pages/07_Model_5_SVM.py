import streamlit as st
import numpy as np
import joblib
import warnings

# Supprimer les warnings sklearn sur les feature names
warnings.filterwarnings('ignore', category=UserWarning, module='sklearn')

# Configuration de la page
st.set_page_config(
    page_title="SVM - Santé Plus",
    page_icon="📦",
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
        <h1 style="color: #1f77b4; margin-bottom: 0.5rem;">📦 Support Vector Machine (SVM)</h1>
    </div>
    """, unsafe_allow_html=True)

# =========================
# Description du modèle
# =========================
st.markdown("""
<div style="background: linear-gradient(135deg, #d62728 0%, #ff9896 100%); 
            padding: 1.5rem; border-radius: 12px; color: white; margin-bottom: 2rem;">
    <p style="font-size: 1.05rem; line-height: 1.8; margin: 0;">
        Le Support Vector Machine (SVM) est un classifieur à marge maximale.
        <br>Il cherche la frontière optimale séparant les tumeurs bénignes et malignes.
    </p>
</div>
""", unsafe_allow_html=True)

# =========================
# Chargement modèle + scaler
# =========================
# Classe wrapper pour le modèle SVM personnalisé
class CustomSVMModel:
    """Wrapper pour un modèle SVM personnalisé avec poids w et biais b"""
    def __init__(self, w, b):
        self.w = np.array(w)
        # b peut être un array (ex: shape (1,)) → extraire un scalaire proprement (évite DeprecationWarning NumPy)
        self.b = float(np.asarray(b).reshape(-1)[0])
    
    def predict(self, X):
        """Prédiction binaire : 0 ou 1"""
        # Calcul : sign(w^T * X + b)
        scores = np.dot(X, self.w) + self.b
        return (scores >= 0).astype(int)
    
    def predict_proba(self, X):
        """Probabilités : utilise une sigmoïde pour convertir les scores en probabilités"""
        scores = np.dot(X, self.w) + self.b
        # Utiliser une sigmoïde pour convertir en probabilités
        # prob = 1 / (1 + exp(-score))
        prob_maligne = 1 / (1 + np.exp(-scores))
        prob_benigne = 1 - prob_maligne
        # Retourner au format [[prob_benigne, prob_maligne], ...]
        return np.column_stack([prob_benigne, prob_maligne])

@st.cache_resource
def load_svm():
    try:
        svm_data = joblib.load("models/svm.pkl")
        scaler = joblib.load("models/scaler.pkl")
    except Exception as e:
        raise FileNotFoundError(f"Impossible de charger les fichiers de modèle : {e}")
    
    # Vérifier si c'est un modèle personnalisé (avec w et b)
    if isinstance(svm_data, dict):
        if 'w' in svm_data and 'b' in svm_data:
            # C'est un modèle SVM personnalisé
            w = svm_data['w']
            b = svm_data['b']
            model = CustomSVMModel(w, b)
        else:
            # Essayer d'extraire un modèle scikit-learn standard
            model = None
            for key in ["svm", "model", "classifier", "svm_model", "estimator"]:
                if key in svm_data:
                    candidate = svm_data[key]
                    if hasattr(candidate, 'predict') and not isinstance(candidate, dict):
                        model = candidate
                        break
            
            # Si aucun modèle trouvé, essayer de prendre le premier objet qui a predict
            if model is None:
                for key, value in svm_data.items():
                    if hasattr(value, 'predict') and not isinstance(value, dict):
                        model = value
                        break
            
            if model is None:
                raise ValueError(f"Impossible d'extraire un modèle SVM valide. Clés disponibles : {list(svm_data.keys())}")
    else:
        # Modèle direct (pas un dict)
        if hasattr(svm_data, 'predict'):
            model = svm_data
        else:
            raise ValueError(f"Le modèle chargé n'a pas de méthode 'predict'. Type : {type(svm_data)}")
    
    return model, scaler

svm_model, scaler = load_svm()

# Vérification que le modèle est valide
if svm_model is None:
    st.error("❌ Erreur : Impossible de charger le modèle SVM.")
    st.stop()

if isinstance(svm_model, dict):
    st.error(f"❌ Erreur : Le modèle SVM est un dictionnaire. Clés disponibles : {list(svm_model.keys())}")
    st.info("💡 Le modèle doit être extrait du dictionnaire. Vérifiez la structure du fichier svm.pkl")
    st.stop()

if not hasattr(svm_model, 'predict'):
    st.error(f"❌ Erreur : L'objet chargé n'a pas de méthode 'predict'. Type : {type(svm_model)}")
    st.stop()

# =========================
# Formulaire des inputs
# =========================
st.markdown("### 🔢 Entrer les caractéristiques de la tumeur")
st.markdown("Remplissez les 22 caractéristiques morphologiques ci-dessous :")

with st.form("svm_form"):
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

    # Probabilité + seuil
    # Vérifier d'abord que svm_model est bien un modèle et non un dict
    if isinstance(svm_model, dict):
        st.error("❌ Erreur : Le modèle SVM n'a pas été correctement chargé (c'est un dictionnaire).")
        st.error(f"Clés disponibles dans le dictionnaire : {list(svm_model.keys())}")
        st.stop()
    
    # Utiliser predict_proba si disponible, sinon utiliser predict
    try:
        if hasattr(svm_model, 'predict_proba'):
            # predict_proba retourne un tableau 2D : [[prob_classe_0, prob_classe_1]]
            proba_result = svm_model.predict_proba(X_scaled)
            if len(proba_result.shape) == 2 and proba_result.shape[1] >= 2:
                y_prob = float(proba_result[0][1])  # Probabilité de la classe 1 (maligne)
            elif len(proba_result.shape) == 2 and proba_result.shape[1] == 1:
                # Une seule classe, utiliser la probabilité disponible
                y_prob = float(proba_result[0][0])
            else:
                # Format inattendu
                y_prob = 0.5
                st.warning(f"⚠️ Format de probabilité inattendu. Shape: {proba_result.shape}")
        else:
            # Si predict_proba n'est pas disponible, utiliser predict
            pred_result = svm_model.predict(X_scaled)
            
            # Vérifier la structure du résultat
            if isinstance(pred_result, np.ndarray):
                if len(pred_result.shape) > 1 and pred_result.shape[1] > 1:
                    # Tableau 2D avec plusieurs colonnes (probabilités)
                    y_prob = float(pred_result[0][1])
                elif len(pred_result.shape) == 1:
                    # Prédiction binaire simple (1D array)
                    y_pred_binary = int(pred_result[0])
                    y_prob = 0.8 if y_pred_binary == 1 else 0.2
                else:
                    # Format inattendu
                    y_pred_binary = int(pred_result.flatten()[0])
                    y_prob = 0.8 if y_pred_binary == 1 else 0.2
            elif isinstance(pred_result, (list, tuple)):
                # Liste ou tuple
                if len(pred_result) > 1 and isinstance(pred_result[0], (list, np.ndarray)):
                    y_prob = float(pred_result[0][1])
                else:
                    y_pred_binary = int(pred_result[0])
                    y_prob = 0.8 if y_pred_binary == 1 else 0.2
            else:
                # Format inattendu, estimer depuis la prédiction
                y_pred_binary = int(pred_result) if not isinstance(pred_result, (list, np.ndarray)) else int(pred_result[0])
                y_prob = 0.8 if y_pred_binary == 1 else 0.2
    except (IndexError, TypeError, AttributeError) as e:
        # Fallback : prédiction binaire simple
        try:
            pred_result = svm_model.predict(X_scaled)
            if isinstance(pred_result, np.ndarray):
                y_pred_binary = int(pred_result.flatten()[0])
            elif isinstance(pred_result, (list, tuple)):
                y_pred_binary = int(pred_result[0])
            else:
                y_pred_binary = int(pred_result)
            y_prob = 0.8 if y_pred_binary == 1 else 0.2
            st.warning(f"⚠️ Utilisation d'une probabilité estimée. Erreur originale: {str(e)}")
        except Exception as e2:
            st.error(f"❌ Erreur lors de la prédiction SVM : {str(e2)}")
            st.error(f"Type du modèle : {type(svm_model)}")
            st.error(f"Type du résultat predict : {type(pred_result) if 'pred_result' in locals() else 'N/A'}")
            st.stop()
    except Exception as e:
        st.error(f"❌ Erreur inattendue lors de la prédiction SVM : {str(e)}")
        st.error(f"Type du modèle : {type(svm_model)}")
        import traceback
        st.code(traceback.format_exc())
        st.stop()
    
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
