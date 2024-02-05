import logging 
import pandas as pd
from zenml import step 

@step
def train_model(df: pd.DataFrame)-> pd.DataFrame:
    """
    Trains the model on the cleaned data

    Args:
        df: the cleaned dataframe
    """
