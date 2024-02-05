import logging
import pandas as pd
from zenml import step 

@step
def evaluate_model(df: pd.Dataframe) -> None:
    """
    Evaluates the model on the cleaned data

    Args:
        df: the cleaned dataframe
    """
    pass
