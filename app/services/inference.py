import joblib
import numpy as np
import os
from .cache import get_from_cache, set_to_cache

model = None

FEATURE_ORDER = [
    "V1","V2","V3","V4","V5","V6","V7","V8","V9","V10",
    "V11","V12","V13","V14","V15","V16","V17","V18","V19","V20",
    "V21","V22","V23","V24","V25","V26","V27","V28","Amount"
]

def load_model():
    global model
    if model is None:
        model_path = os.path.join(os.path.dirname(__file__), "..", "ml", "model.pkl")
        model_path = os.path.abspath(model_path)
        model = joblib.load(model_path)

def predict_anomaly(data: dict):
    load_model()

    values_list = [data[f] for f in FEATURE_ORDER]

    # Create cache key
    key = tuple(values_list)

    # Check cache
    cached = get_from_cache(key)
    if cached is not None:
        print("⚡ Cache hit")
        return cached

    # Convert to numpy
    values = np.array(values_list).reshape(1, -1)

    # Predict
    pred = model.predict(values)[0]
    result = 1 if pred == -1 else 0

    print("Prediction:", pred)

    #  Store in cache
    set_to_cache(key, result)

    return result