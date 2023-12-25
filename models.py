# models.py

# Importing required libraries
from sklearn.externals import joblib
from config import MODEL_CONFIG

class Model:
    def __init__(self):
        self.model = self.load_model()

    def load_model(self):
        try:
            model = joblib.load(MODEL_CONFIG['MODEL_PATH'] + MODEL_CONFIG['MODEL_NAME'])
            return model
        except Exception as e:
            print(f"Error loading the model: {e}")
            return None

    def predict(self, data):
        try:
            prediction = self.model.predict(data)
            return prediction
        except Exception as e:
            print(f"Error making prediction: {e}")
            return None
