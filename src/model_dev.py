from sklearn.linear_model import LinearRegression
import pickle
import os

class ModelDevelopment:
    def __init__(self):
        self.model = LinearRegression()

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def save_model(self, model_directory):
        if not os.path.exists(model_directory):
            os.makedirs(model_directory)
        model_path = os.path.join(model_directory, 'trained_model.pkl')
        with open(model_path, 'wb') as f:
            pickle.dump(self.model, f)
        return model_path
    
    def load_model(self, model_path):
        # Méthode pour charger un modèle préalablement entraîné
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        return model
