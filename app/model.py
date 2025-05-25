import pickle
import numpy as np

class MLModel:
    def __init__(self, model_path: str):
        with open(model_path, "rb") as f:
            self.model = pickle.load(f)

    def predict(self, features: list[float]) -> float:
        if not isinstance(features, list) or not all(isinstance(x, (int, float)) for x in features):
            raise ValueError("Features must be a list of numbers.")
        features = np.array(features).reshape(1, -1)
        return self.model.predict(features)[0]