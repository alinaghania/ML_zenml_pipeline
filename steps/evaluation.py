import logging
from zenml import step
from src.evaluation import ModelEvaluation
import pandas as pd

@step
def evaluate_model(
    model_path: str, 
    X_test: pd.DataFrame, 
    y_test: pd.Series
) -> float:
    """
    Evaluate the trained model with test data.

    Args:
        model_path: Path to the saved trained model.
        X_test: Testing data features.
        y_test: Testing data target.

    Returns:
        r2: R-squared, coefficient of determination.
    """
    try:
        # Load the model
        model = ModelEvaluation.load_model(model_path)

        # Evaluate the model
        r2 = ModelEvaluation.evaluate_model(model, X_test, y_test)  # Directly receive R^2
        
        # Log only the R-squared metric
        logging.info(f"Model R-squared: {r2}")
        
        # Return only the R-squared metric
        return r2
    except Exception as e:
        logging.error(f"Error in model evaluation: {e}")
        raise e