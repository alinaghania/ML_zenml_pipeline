import logging
from zenml import step
from src.model_dev import ModelDevelopment  
import pandas as pd
import os

@step
def train_model(
    X_train: pd.DataFrame, 
    y_train: pd.Series
) -> str:
    """
    Trains the model on the cleaned and preprocessed data.

    Args:
        X_train: Training data features.
        y_train: Training data target.

    Returns:
        model_path: Path where the trained model is saved.
    """
    try:
        # Initialize and train the model
        model_dev = ModelDevelopment()
    
        # Vérifie si un modèle est déjà enregistré
        model_path = 'saved_model/trained_model.pkl'

        if os.path.exists(model_path):
            model = model_dev.load_model(model_path)  
        else:
            # Si aucun modèle n'est enregistré, entraînez-en un nouveau
            model = model_dev.train(X_train, y_train)
            model_dev.save_model(model_path)
        
        return model_path
    except Exception as e:
        logging.error(f"Error in training model: {e}")
        raise e
