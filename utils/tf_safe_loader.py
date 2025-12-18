"""
Utilitaire pour charger TensorFlow de manière sécurisée et éviter les segfaults
"""
import os
import sys

# Configuration des variables d'environnement AVANT l'import TensorFlow
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_DISABLE_MKL'] = '1'
os.environ['OMP_NUM_THREADS'] = '1'
os.environ['MKL_NUM_THREADS'] = '1'

def safe_import_tensorflow():
    """
    Importe TensorFlow de manière sécurisée avec gestion d'erreurs
    """
    try:
        import tensorflow as tf
        
        # Configuration supplémentaire pour éviter les segfaults
        tf.get_logger().setLevel('ERROR')
        
        # Limiter les threads pour éviter les problèmes de mémoire
        try:
            tf.config.threading.set_inter_op_parallelism_threads(1)
            tf.config.threading.set_intra_op_parallelism_threads(1)
        except:
            pass  # Ignorer si la configuration échoue
        
        # Désactiver les optimisations qui peuvent causer des segfaults
        try:
            tf.config.set_soft_device_placement(True)
        except:
            pass
        
        return tf
    except Exception as e:
        print(f"Warning: Could not import TensorFlow safely: {e}")
        return None

def setup_keras_compatibility(tf):
    """
    Configure la compatibilité Keras 3.x vers TensorFlow 2.x
    """
    if tf is None:
        return False
    
    try:
        import types
        # Si Keras (standalone) est installé, on l'utilise.
        # IMPORTANT: ne pas forcer sys.modules['keras'] = tf.keras (LazyLoader) → peut provoquer une récursion infinie
        # avec les versions récentes de TensorFlow.
        keras_mod = None
        keras_version = None
        try:
            import keras as _keras  # standalone keras (2.x ou 3.x)
            keras_mod = _keras
            keras_version = getattr(_keras, "__version__", None)
        except Exception:
            keras_mod = None
            keras_version = None

        # Si Keras 3 est présent, les imports keras.src.* existent déjà → rien à faire.
        if isinstance(keras_version, str) and keras_version.startswith("3"):
            return True

        # Base pour mapper les symboles: priorité à Keras standalone 2.x si dispo, sinon tf.keras
        base_keras = keras_mod if keras_mod is not None else tf.keras

        # 2) Créer les conteneurs "packages" keras.src.*
        for name in [
            'keras.src',
            'keras.src.models',
            'keras.src.models.sequential',
            'keras.src.saving',
            'keras.src.saving.keras_saveable',
        ]:
            if name not in sys.modules or not isinstance(sys.modules.get(name), types.ModuleType):
                sys.modules[name] = types.ModuleType(name)

        # 3) Injecter les symboles attendus par les pickles (Keras 3)
        sys.modules['keras.src.models'].Sequential = getattr(base_keras, "Sequential", None) or tf.keras.Sequential
        sys.modules['keras.src.models'].Model = getattr(base_keras, "Model", None) or tf.keras.Model
        sys.modules['keras.src.models.sequential'].Sequential = getattr(base_keras, "Sequential", None) or tf.keras.Sequential

        # keras.src.saving.keras_saveable.KerasSaveable
        sys.modules['keras.src.saving.keras_saveable'].KerasSaveable = object

        # 4) Mapper les sous-modules Keras “classiques”
        sys.modules['keras.src.layers'] = getattr(base_keras, "layers", tf.keras.layers)
        sys.modules['keras.src.optimizers'] = getattr(base_keras, "optimizers", tf.keras.optimizers)
        sys.modules['keras.src.losses'] = getattr(base_keras, "losses", tf.keras.losses)
        sys.modules['keras.src.metrics'] = getattr(base_keras, "metrics", tf.keras.metrics)
        # Certaines versions de TF n'exposent pas tf.keras.saving → fallback sur un module vide
        saving_mod = getattr(base_keras, 'saving', None) or getattr(tf.keras, 'saving', None)
        if saving_mod is not None:
            sys.modules['keras.src.saving'] = saving_mod
        else:
            if 'keras.src.saving' not in sys.modules or not isinstance(sys.modules.get('keras.src.saving'), types.ModuleType):
                sys.modules['keras.src.saving'] = types.ModuleType('keras.src.saving')

        return True
    except Exception as e:
        print(f"Warning: Could not setup Keras compatibility: {e}")
        return False

