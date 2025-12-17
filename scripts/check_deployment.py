"""
Script simple pour vérifier que l'application est prête pour le déploiement
"""
import os
import sys

def check_file_exists(filepath, description):
    """Vérifie qu'un fichier existe"""
    if os.path.exists(filepath):
        print(f"✅ {description}: {filepath}")
        return True
    else:
        print(f"❌ {description} manquant: {filepath}")
        return False

def main():
    """Vérifie tous les fichiers nécessaires pour le déploiement"""
    print("=== Vérification des fichiers de déploiement ===\n")
    
    required_files = [
        ("app.py", "Application principale"),
        ("requirements.txt", "Dépendances Python"),
        ("Dockerfile", "Configuration Docker"),
        ("render.yaml", "Configuration Render"),
        ("runtime.txt", "Version Python"),
        ("Procfile", "Commande de démarrage"),
    ]
    
    all_ok = True
    for filepath, description in required_files:
        if not check_file_exists(filepath, description):
            all_ok = False
    
    # Vérifier les modèles
    print("\n=== Vérification des modèles ===")
    if os.path.exists("models"):
        model_files = os.listdir("models")
        if model_files:
            print(f"✅ {len(model_files)} fichiers de modèles trouvés")
            for f in model_files:
                print(f"   - {f}")
        else:
            print("❌ Le dossier models/ est vide")
            all_ok = False
    else:
        print("❌ Le dossier models/ n'existe pas")
        all_ok = False
    
    # Résumé
    print("\n=== Résumé ===")
    if all_ok:
        print("✅ Tous les fichiers nécessaires sont présents")
        print("✅ Prêt pour le déploiement")
        sys.exit(0)
    else:
        print("❌ Certains fichiers manquent")
        print("❌ Corrigez les erreurs avant de déployer")
        sys.exit(1)

if __name__ == "__main__":
    main()

