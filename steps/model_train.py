import logging
from zenml import step
from src.model_dev import ModelDevelopment  
import pandas as pd

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
        model_dev.train(X_train, y_train)
        
        # Save the model
        model_path = model_dev.save_model('saved_model')  
        
        logging.info(f"Model trained and saved at {model_path}")
        return model_path
    except Exception as e:
        logging.error(f"Error in training model: {e}")
        raise e
