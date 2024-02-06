import logging 
import pandas as pd
from zenml import step
from typing_extensions import Annotated
from types import Tuple

from src.data_cleaning import DataCleaning, DataDivideStrategy , DataPreProcessStrategy

@step
def clean_df(df: pd.DataFrame) -> Tuple[
    Annotated[pd.DataFrame, 'X_train'],
    Annotated[pd.DataFrame, 'X_test'],
    Annotated[pd.Series, 'y_train'],
    Annotated[pd.Series, 'y_test'],
]:
    """
    Step to clean and split the data

    Args:
        df : raw data
    Returns:
        X_train : Training data
        X_test : Testing data
        
        y_train : Training target
        y_test : Testing target
    """

    try:
        process_strategy = DataPreProcessStrategy()
        data_cleaning = DataCleaning(df, process_strategy)

        processed_data = data_cleaning.handle_data()
        divide_strategy = DataDivideStrategy()

        data_cleaning = DataCleaning(processed_data, divide_strategy)

        X_train, X_test, y_train, y_test = data_cleaning.handle_data()
        logging.info(f"Data cleaning and splitting done successfully")
        
    except Exception as e:
        logging.error(f"Error in cleaning and splitting data: {e}")
        raise e
        

