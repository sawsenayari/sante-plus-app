import streamlit as st
from streamlit_option_menu import option_menu

# =========================
# Configuration de la page
# =========================
st.set_page_config(
    page_title="Santé Plus",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================
# Chargement du CSS personnalisé
# =========================
def load_css():
    try:
        with open("style.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except:
        pass

load_css()

# =========================
# Barre de navigation
# =========================
selected = option_menu(
    menu_title=None,
    options=[
        "Accueil",
        "Comparaison",
        "GRU-SVM",
        "Linear Regression",
        "MLP",
        "k-NN",
        "Softmax Regression",
        "SVM",
        "À Propos"
    ],
    icons=[
        "house",
        "bar-chart",
        "activity",
        "graph-up",
        "layers",
        "diagram-3",
        "arrow-repeat",
        "bounding-box",
        "info-circle"
    ],
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#f8f9fa"},
        "icon": {"color": "#1f77b4", "font-size": "18px"},
        "nav-link": {
            "font-size": "16px",
            "text-align": "center",
            "margin": "0px",
            "padding": "12px",
            "--hover-color": "#e9ecef",
        },
        "nav-link-selected": {"background-color": "#1f77b4", "color": "white"},
    }
)

# =========================
# Navigation vers les pages
# =========================
page_mapping = {
    "Accueil": "pages/01_Accueil.py",
    "Comparaison": "pages/09_Comparaison_Modeles.py",
    "GRU-SVM": "pages/02_Modele_1_GRU_SVM.py",
    "Linear Regression": "pages/03_Modele_2_Linear_Regression.py",
    "MLP": "pages/04_Modele_3_MLP.py",
    "k-NN": "pages/07_Modele_6_knn.py",
    "Softmax Regression": "pages/05_Modele_4_Softmax.py",
    "SVM": "pages/07_Model_5_SVM.py",
    "À Propos": "pages/08_A_Propos.py"
}

if selected in page_mapping:
    st.switch_page(page_mapping[selected])
