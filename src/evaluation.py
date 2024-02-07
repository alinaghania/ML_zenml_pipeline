import pickle
from sklearn.metrics import mean_squared_error, r2_score

class ModelEvaluation:
    @staticmethod
    def load_model(model_path: str):
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        return model

    @staticmethod
    def evaluate_model(model, X_test, y_test):
        predictions = model.predict(X_test)
        r2 = r2_score(y_test, predictions)
        return r2  