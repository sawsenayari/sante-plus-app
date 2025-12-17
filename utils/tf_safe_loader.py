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
        
        # Mapper keras vers tf.keras
        if 'keras' not in sys.modules:
            sys.modules['keras'] = tf.keras
        
        # Créer les modules factices pour keras.src.*
        modules_config = {
            'keras.src': types.ModuleType('keras.src'),
            'keras.src.models': types.ModuleType('keras.src.models'),
            'keras.src.models.sequential': types.ModuleType('keras.src.models.sequential'),
            'keras.src.layers': tf.keras.layers,
            'keras.src.optimizers': tf.keras.optimizers,
            'keras.src.losses': tf.keras.losses,
            'keras.src.metrics': tf.keras.metrics,
            'keras.src.saving': tf.keras.saving,
            'keras.src.saving.keras_saveable': types.ModuleType('keras.src.saving.keras_saveable')
        }
        
        # Configurer les modules
        if 'keras.src.models' not in sys.modules:
            mod = modules_config['keras.src.models']
            mod.Sequential = tf.keras.Sequential
            mod.Model = tf.keras.Model
            sys.modules['keras.src.models'] = mod
        
        if 'keras.src.models.sequential' not in sys.modules:
            mod = modules_config['keras.src.models.sequential']
            mod.Sequential = tf.keras.Sequential
            sys.modules['keras.src.models.sequential'] = mod
        
        if 'keras.src.saving.keras_saveable' not in sys.modules:
            mod = modules_config['keras.src.saving.keras_saveable']
            mod.KerasSaveable = object
            sys.modules['keras.src.saving.keras_saveable'] = mod
        
        # Mapper les autres modules
        for module_name, module_obj in modules_config.items():
            if module_name not in sys.modules and not isinstance(module_obj, types.ModuleType):
                sys.modules[module_name] = module_obj
        
        return True
    except Exception as e:
        print(f"Warning: Could not setup Keras compatibility: {e}")
        return False

