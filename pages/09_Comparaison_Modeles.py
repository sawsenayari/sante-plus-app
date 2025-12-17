import streamlit as st
import numpy as np
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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

# Classe wrapper pour le modèle SVM personnalisé
class CustomSVMModel:
    """Wrapper pour un modèle SVM personnalisé avec poids w et biais b"""
    def __init__(self, w, b):
        self.w = np.array(w)
        self.b = float(b)
    
    def predict(self, X):
        """Prédiction binaire : 0 ou 1"""
        scores = np.dot(X, self.w) + self.b
        return (scores >= 0).astype(int)
    
    def predict_proba(self, X):
        """Probabilités : utilise une sigmoïde pour convertir les scores en probabilités"""
        scores = np.dot(X, self.w) + self.b
        prob_maligne = 1 / (1 + np.exp(-scores))
        prob_benigne = 1 - prob_maligne
        return np.column_stack([prob_benigne, prob_maligne])

# Configuration de la page
st.set_page_config(
    page_title="Comparaison des Modèles - Santé Plus",
    page_icon="📊",
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
        <h1 style="color: #1f77b4; margin-bottom: 0.5rem;">📊 Comparaison des Modèles</h1>
    </div>
    """, unsafe_allow_html=True)

# =========================
# Description
# =========================
st.markdown("""
<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            padding: 1.5rem; border-radius: 12px; color: white; margin-bottom: 2rem;">
    <p style="font-size: 1.05rem; line-height: 1.8; margin: 0;">
        Comparez les prédictions de <strong>tous les modèles</strong> avec les mêmes caractéristiques.
        <br>Cette page vous permet d'évaluer la cohérence et les différences entre les différents algorithmes de Machine Learning.
    </p>
</div>
""", unsafe_allow_html=True)

# =========================
# Chargement de tous les modèles
# =========================
@st.cache_resource
def load_all_models():
    """Charge tous les modèles et le scaler"""
    try:
        # S'assurer que Keras/TensorFlow sont importés avant de charger les modèles
        try:
            import tensorflow as tf
            tf.get_logger().setLevel('ERROR')
            import keras
        except ImportError:
            pass
        
        scaler = joblib.load("models/scaler.pkl")
        
        # Linear Regression
        lin_reg = joblib.load("models/linear_regression.pkl")
        
        # GRU-SVM (nécessite Keras)
        try:
            gru_svm_data = joblib.load("models/gru_svm.pkl")
            if isinstance(gru_svm_data, dict):
                gru_svm_model = gru_svm_data.get("svm", gru_svm_data.get("model", None))
            else:
                gru_svm_model = gru_svm_data
        except Exception as e:
            st.warning(f"Erreur lors du chargement de GRU-SVM : {e}")
            gru_svm_model = None
        
        # MLP (nécessite Keras)
        try:
            mlp_model = joblib.load("models/MLP.pkl")
        except Exception as e:
            st.warning(f"Erreur lors du chargement de MLP : {e}")
            mlp_model = None
        
        # Softmax
        try:
            softmax_model = joblib.load("models/softmax.pkl")
        except Exception as e:
            st.warning(f"Erreur lors du chargement de Softmax : {e}")
            softmax_model = None
        
        # k-NN
        knn_model = joblib.load("models/knn.pkl")
        
        # SVM - peut être un modèle personnalisé avec w et b
        try:
            svm_data = joblib.load("models/svm.pkl")
            if isinstance(svm_data, dict):
                if 'w' in svm_data and 'b' in svm_data:
                    # Modèle SVM personnalisé
                    svm_model = CustomSVMModel(svm_data['w'], svm_data['b'])
                else:
                    # Essayer d'extraire un modèle scikit-learn
                    svm_model = None
                    for key in ["svm", "model", "classifier", "svm_model", "estimator"]:
                        if key in svm_data and hasattr(svm_data[key], 'predict'):
                            svm_model = svm_data[key]
                            break
                    if svm_model is None:
                        for key, value in svm_data.items():
                            if hasattr(value, 'predict') and not isinstance(value, dict):
                                svm_model = value
                                break
            else:
                svm_model = svm_data if hasattr(svm_data, 'predict') else None
        except Exception as e:
            st.warning(f"Erreur lors du chargement de SVM : {e}")
            svm_model = None
        
        return {
            "scaler": scaler,
            "Linear Regression": lin_reg,
            "GRU-SVM": gru_svm_model,
            "MLP": mlp_model,
            "Softmax Regression": softmax_model,
            "k-NN": knn_model,
            "SVM": svm_model
        }
    except Exception as e:
        # Ne pas arrêter complètement, retourner ce qui a pu être chargé
        st.warning(f"⚠️ Certains modèles n'ont pas pu être chargés : {e}")
        # Retourner au moins le scaler et les modèles de base
        return {
            "scaler": scaler if 'scaler' in locals() else None,
            "Linear Regression": lin_reg if 'lin_reg' in locals() else None,
            "GRU-SVM": gru_svm_model if 'gru_svm_model' in locals() else None,
            "MLP": mlp_model if 'mlp_model' in locals() else None,
            "Softmax Regression": softmax_model if 'softmax_model' in locals() else None,
            "k-NN": knn_model if 'knn_model' in locals() else None,
            "SVM": svm_model if 'svm_model' in locals() else None
        }

models = load_all_models()
scaler = models.get("scaler")
if scaler is None:
    st.error("❌ Impossible de charger le scaler. L'application ne peut pas fonctionner.")
    st.stop()

# =========================
# Formulaire d'entrée
# =========================
st.markdown("### 🔢 Entrer les caractéristiques de la tumeur")
st.markdown("Remplissez les 22 caractéristiques morphologiques ci-dessous :")

with st.form("comparison_form"):
    st.markdown("#### Caractéristiques moyennes (Mean)")
    col1, col2, col3 = st.columns(3)

    with col1:
        radius_mean = st.number_input("Radius Mean", min_value=0.0, value=0.0, step=0.1, format="%.2f", help="Rayon moyen des cellules")
        texture_mean = st.number_input("Texture Mean", min_value=0.0, value=0.0, step=0.1, format="%.2f", help="Texture moyenne")
        area_mean = st.number_input("Area Mean", min_value=0.0, value=0.0, step=1.0, format="%.2f", help="Surface moyenne")
        smoothness_mean = st.number_input("Smoothness Mean", min_value=0.0, value=0.0, step=0.001, format="%.4f", help="Lissage moyen")

    with col2:
        compactness_mean = st.number_input("Compactness Mean", min_value=0.0, value=0.0, step=0.001, format="%.4f", help="Compacité moyenne")
        concavity_mean = st.number_input("Concavity Mean", min_value=0.0, value=0.0, step=0.001, format="%.4f", help="Concavité moyenne")
        concave_points_mean = st.number_input("Concave Points Mean", min_value=0.0, value=0.0, step=0.001, format="%.4f", help="Points concaves moyens")
        symmetry_mean = st.number_input("Symmetry Mean", min_value=0.0, value=0.0, step=0.001, format="%.4f", help="Symétrie moyenne")

    with col3:
        fractal_dimension_mean = st.number_input("Fractal Dimension Mean", min_value=0.0, value=0.0, step=0.001, format="%.4f", help="Dimension fractale moyenne")
        radius_se = st.number_input("Radius SE", min_value=0.0, value=0.0, step=0.1, format="%.2f", help="Rayon (erreur standard)")
        area_se = st.number_input("Area SE", min_value=0.0, value=0.0, step=1.0, format="%.2f", help="Surface (erreur standard)")
        compactness_se = st.number_input("Compactness SE", min_value=0.0, value=0.0, step=0.001, format="%.4f", help="Compacité (erreur standard)")

    st.markdown("#### Caractéristiques d'erreur standard (SE)")
    col4, col5, col6 = st.columns(3)

    with col4:
        concavity_se = st.number_input("Concavity SE", min_value=0.0, value=0.0, step=0.001, format="%.4f", help="Concavité (erreur standard)")
        concave_points_se = st.number_input("Concave Points SE", min_value=0.0, value=0.0, step=0.001, format="%.4f", help="Points concaves (erreur standard)")

    st.markdown("#### Caractéristiques les plus défavorables (Worst)")
    col7, col8, col9 = st.columns(3)

    with col7:
        radius_worst = st.number_input("Radius Worst", min_value=0.0, value=0.0, step=0.1, format="%.2f", help="Rayon le plus défavorable")
        texture_worst = st.number_input("Texture Worst", min_value=0.0, value=0.0, step=0.1, format="%.2f", help="Texture la plus défavorable")
        area_worst = st.number_input("Area Worst", min_value=0.0, value=0.0, step=1.0, format="%.2f", help="Surface la plus défavorable")

    with col8:
        smoothness_worst = st.number_input("Smoothness Worst", min_value=0.0, value=0.0, step=0.001, format="%.4f", help="Lissage le plus défavorable")
        compactness_worst = st.number_input("Compactness Worst", min_value=0.0, value=0.0, step=0.001, format="%.4f", help="Compacité la plus défavorable")
        concavity_worst = st.number_input("Concavity Worst", min_value=0.0, value=0.0, step=0.001, format="%.4f", help="Concavité la plus défavorable")

    with col9:
        concave_points_worst = st.number_input("Concave Points Worst", min_value=0.0, value=0.0, step=0.001, format="%.4f", help="Points concaves les plus défavorables")
        symmetry_worst = st.number_input("Symmetry Worst", min_value=0.0, value=0.0, step=0.001, format="%.4f", help="Symétrie la plus défavorable")

    col_submit, _, _ = st.columns([1, 2, 2])
    with col_submit:
        submitted = st.form_submit_button("🔍 Comparer tous les modèles", use_container_width=True, type="primary")

# =========================
# Prédictions avec tous les modèles
# =========================
if submitted:
    # Construction du tableau d'entrée
    X_22 = np.array([[
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
    X_scaled_22 = scaler.transform(X_22)

    # Dictionnaire pour stocker les résultats
    results = {}

    # Prédiction avec chaque modèle
    with st.spinner("Calcul des prédictions avec tous les modèles..."):
        # Linear Regression
        try:
            score = models["Linear Regression"].predict(X_scaled_22)[0]
            prob = max(0, min(1, score))  # Clamp entre 0 et 1
            pred = 1 if prob >= 0.5 else 0
            results["Linear Regression"] = {
                "probabilite": float(prob),  # Convertir en float Python
                "prediction": pred,
                "score": float(score),
                "type": "score"
            }
        except Exception as e:
            results["Linear Regression"] = {"error": str(e)}

        # GRU-SVM
        try:
            if models["GRU-SVM"] is None:
                results["GRU-SVM"] = {"error": "Modèle non chargé (Keras requis)"}
            else:
                EXPECTED_FEATURES = 32
                n_missing = EXPECTED_FEATURES - X_scaled_22.shape[1]
                X_final = np.hstack([X_scaled_22, np.zeros((1, n_missing))])
                pred = models["GRU-SVM"].predict(X_final)[0]
                # Pour GRU-SVM, on n'a pas de probabilité directe, on utilise la prédiction
                prob = 0.8 if pred == 1 else 0.2  # Estimation
                results["GRU-SVM"] = {
                    "probabilite": float(prob),  # Convertir en float Python
                    "prediction": pred,
                    "type": "binary"
                }
        except Exception as e:
            results["GRU-SVM"] = {"error": str(e)}

        # MLP
        try:
            if models["MLP"] is None:
                results["MLP"] = {"error": "Modèle non chargé (Keras requis)"}
            else:
                prob = models["MLP"].predict(X_scaled_22)[0][0]
                pred = 1 if prob >= 0.5 else 0
                results["MLP"] = {
                    "probabilite": float(prob),  # Convertir en float Python
                    "prediction": pred,
                    "type": "probability"
                }
        except Exception as e:
            results["MLP"] = {"error": str(e)}

        # Softmax Regression
        try:
            if models["Softmax Regression"] is None:
                results["Softmax Regression"] = {"error": "Modèle non chargé"}
            else:
                prob = models["Softmax Regression"].predict(X_scaled_22)[0][1]
                pred = 1 if prob >= 0.5 else 0
                results["Softmax Regression"] = {
                    "probabilite": float(prob),  # Convertir en float Python
                    "prediction": pred,
                    "type": "probability"
                }
        except Exception as e:
            results["Softmax Regression"] = {"error": str(e)}

        # k-NN
        try:
            if models["k-NN"] is None:
                results["k-NN"] = {"error": "Modèle non chargé"}
            else:
                prob = models["k-NN"].predict_proba(X_scaled_22)[0][1]
                pred = 1 if prob >= 0.5 else 0
                results["k-NN"] = {
                    "probabilite": float(prob),  # Convertir en float Python
                    "prediction": pred,
                    "type": "probability"
                }
        except Exception as e:
            results["k-NN"] = {"error": str(e)}

        # SVM
        try:
            if models["SVM"] is None:
                results["SVM"] = {"error": "Modèle non chargé"}
            else:
                svm_model = models["SVM"]
                # Utiliser predict_proba si disponible
                if hasattr(svm_model, 'predict_proba'):
                    prob = svm_model.predict_proba(X_scaled_22)[0][1]
                else:
                    # Utiliser predict et estimer une probabilité
                    pred_result = svm_model.predict(X_scaled_22)
                    if isinstance(pred_result, np.ndarray):
                        y_pred_binary = int(pred_result[0])
                    else:
                        y_pred_binary = int(pred_result[0]) if hasattr(pred_result, '__getitem__') else int(pred_result)
                    prob = 0.8 if y_pred_binary == 1 else 0.2
                
                pred = 1 if prob >= 0.5 else 0
                results["SVM"] = {
                    "probabilite": float(prob),  # Convertir en float Python
                    "prediction": pred,
                    "type": "probability"
                }
        except Exception as e:
            results["SVM"] = {"error": str(e)}

    st.markdown("---")
    st.markdown("### 📊 Résultats de la comparaison")

    # Affichage des erreurs s'il y en a
    errors_found = {name: r for name, r in results.items() if "error" in r}
    if errors_found:
        st.warning("⚠️ Certains modèles ont rencontré des erreurs :")
        for model_name, error_result in errors_found.items():
            st.error(f"**{model_name}** : {error_result['error']}")

    # Création du DataFrame pour l'affichage
    comparison_data = []
    for model_name, result in results.items():
        if "error" not in result:
            comparison_data.append({
                "Modèle": model_name,
                "Probabilité de malignité": f"{result['probabilite']:.4f}",
                "Prédiction": "⚠️ Maligne" if result['prediction'] == 1 else "✅ Bénigne",
                "Confiance": "Élevée" if abs(result['probabilite'] - 0.5) > 0.3 else "Moyenne" if abs(result['probabilite'] - 0.5) > 0.15 else "Faible"
            })

    if comparison_data:
        df = pd.DataFrame(comparison_data)
        
        # Affichage du tableau
        st.dataframe(df, use_container_width=True, hide_index=True)

        # Statistiques de consensus
        st.markdown("#### 📈 Analyse de consensus")
        
        col_stat1, col_stat2, col_stat3, col_stat4 = st.columns(4)
        
        benign_count = sum(1 for r in results.values() if "error" not in r and r["prediction"] == 0)
        malign_count = sum(1 for r in results.values() if "error" not in r and r["prediction"] == 1)
        total_models = len([r for r in results.values() if "error" not in r])
        
        if total_models > 0:
            avg_prob = float(np.mean([r["probabilite"] for r in results.values() if "error" not in r]))  # Convertir en float Python
        else:
            avg_prob = 0.0
        
        with col_stat1:
            st.metric("Modèles testés", total_models)
        with col_stat2:
            if total_models > 0:
                st.metric("Prédictions Bénignes", benign_count, f"{benign_count/total_models*100:.1f}%")
            else:
                st.metric("Prédictions Bénignes", benign_count)
        with col_stat3:
            if total_models > 0:
                st.metric("Prédictions Malignes", malign_count, f"{malign_count/total_models*100:.1f}%")
            else:
                st.metric("Prédictions Malignes", malign_count)
        with col_stat4:
            st.metric("Probabilité moyenne", f"{avg_prob:.4f}")

        # Visualisation des probabilités
        st.markdown("#### 📊 Graphique de comparaison des probabilités")
        
        fig, ax = plt.subplots(figsize=(12, 6))
        model_names = [r["Modèle"] for r in comparison_data]
        probs = [float(r["Probabilité de malignité"]) for r in comparison_data]
        colors = ['#d62728' if p >= 0.5 else '#2ca02c' for p in probs]
        
        bars = ax.barh(model_names, probs, color=colors, alpha=0.7)
        ax.axvline(x=0.5, color='gray', linestyle='--', linewidth=2, label='Seuil de décision (0.5)')
        ax.set_xlabel('Probabilité de malignité', fontsize=12, fontweight='bold')
        ax.set_ylabel('Modèles', fontsize=12, fontweight='bold')
        ax.set_xlim(0, 1)
        ax.set_title('Comparaison des probabilités de malignité par modèle', fontsize=14, fontweight='bold', pad=20)
        ax.legend()
        ax.grid(axis='x', alpha=0.3)
        
        # Ajouter les valeurs sur les barres
        for i, (bar, prob) in enumerate(zip(bars, probs)):
            ax.text(prob + 0.02, i, f'{prob:.3f}', va='center', fontweight='bold')
        
        plt.tight_layout()
        st.pyplot(fig)

        # Analyse de consensus
        if total_models > 0:
            st.markdown("#### 🤝 Consensus des modèles")
            
            if benign_count == total_models:
                st.success(f"✅ **Consensus total** : Tous les {total_models} modèles prédisent une tumeur **BÉNIGNE**")
            elif malign_count == total_models:
                st.error(f"⚠️ **Consensus total** : Tous les {total_models} modèles prédisent une tumeur **MALIGNE**")
            else:
                consensus_rate = max(benign_count, malign_count) / total_models * 100
                st.warning(f"⚠️ **Consensus partiel** : {max(benign_count, malign_count)}/{total_models} modèles ({consensus_rate:.1f}%) sont d'accord")
                
                if benign_count > malign_count:
                    st.info(f"Majorité en faveur d'une tumeur **BÉNIGNE** ({benign_count}/{total_models} modèles)")
                else:
                    st.info(f"Majorité en faveur d'une tumeur **MALIGNE** ({malign_count}/{total_models} modèles)")

        # Détails par modèle
        st.markdown("#### 🔍 Détails par modèle")
        
        for model_name, result in results.items():
            if "error" not in result:
                col_detail1, col_detail2 = st.columns([2, 3])
                
                with col_detail1:
                    if result["prediction"] == 1:
                        st.markdown(f"""
                        <div style="background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%); 
                                    padding: 1rem; border-radius: 10px; margin-bottom: 1rem;">
                            <h4 style="color: #d62728; margin: 0;">{model_name}</h4>
                            <p style="margin: 0.5rem 0 0 0; font-weight: bold;">⚠️ MALIGNE</p>
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown(f"""
                        <div style="background: linear-gradient(135deg, #84fab0 0%, #8fd3f4 100%); 
                                    padding: 1rem; border-radius: 10px; margin-bottom: 1rem;">
                            <h4 style="color: #2ca02c; margin: 0;">{model_name}</h4>
                            <p style="margin: 0.5rem 0 0 0; font-weight: bold;">✅ BÉNIGNE</p>
                        </div>
                        """, unsafe_allow_html=True)
                
                with col_detail2:
                    prob = float(result["probabilite"])  # Convertir en float Python pour Streamlit
                    st.progress(prob, text=f"Probabilité de malignité : {prob:.2%}")
            else:
                st.error(f"Erreur avec {model_name}: {result['error']}")

    st.info("⚠️ **Important** : Cette application est un outil d'aide à la décision et ne remplace pas un diagnostic médical professionnel.")

