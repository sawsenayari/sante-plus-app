"""
Script simple de validation des modèles ML
Vérifie que les modèles existent et ont une taille valide avant déploiement
"""
import os
import sys
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def validate_model_file(model_path, model_name):
    """Valide qu'un fichier de modèle existe et a une taille valide"""
    try:
        if not os.path.exists(model_path):
            logger.error(f"❌ {model_name}: Fichier non trouvé - {model_path}")
            return False
        
        # Vérifier la taille du fichier (doit être > 0)
        file_size = os.path.getsize(model_path)
        if file_size == 0:
            logger.error(f"❌ {model_name}: Fichier vide - {model_path}")
            return False
        
        # Convertir en KB pour affichage
        size_kb = file_size / 1024
        logger.info(f"✅ {model_name}: Fichier trouvé ({size_kb:.2f} KB)")
        return True
        
    except Exception as e:
        logger.error(f"❌ {model_name}: Erreur lors de la validation - {str(e)}")
        return False

def main():
    """Valide tous les modèles nécessaires"""
    logger.info("=== Validation des modèles ML ===")
    
    models_dir = "models"
    if not os.path.exists(models_dir):
        logger.error(f"❌ Répertoire {models_dir} non trouvé")
        sys.exit(1)
    
    # Liste des modèles requis
    required_models = {
        "linear_regression": "linear_regression.pkl",
        "knn": "knn.pkl",
        "svm": "svm.pkl",
        "MLP": "MLP.pkl",
        "softmax": "softmax.pkl",
        "gru_svm": "gru_svm.pkl",
        "scaler": "scaler.pkl"
    }
    
    results = {}
    all_valid = True
    
    for model_name, filename in required_models.items():
        model_path = os.path.join(models_dir, filename)
        is_valid = validate_model_file(model_path, model_name)
        results[model_name] = is_valid
        if not is_valid:
            all_valid = False
    
    # Résumé
    logger.info("\n=== Résumé ===")
    valid_count = sum(1 for v in results.values() if v)
    total_count = len(results)
    
    logger.info(f"Modèles validés: {valid_count}/{total_count}")
    
    if all_valid:
        logger.info("✅ Tous les modèles sont valides")
        sys.exit(0)
    else:
        logger.error("❌ Certains modèles sont invalides")
        sys.exit(1)

if __name__ == "__main__":
    main()

