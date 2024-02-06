import logging 
import pandas as pd
from zenml import step
from typing_extensions import Annotated
from typing import Tuple

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
        processed_data = DataCleaning(df, DataPreProcessStrategy()).handle_data()

        # Ensure the result is of the expected type
        if isinstance(processed_data, tuple):
            processed_data = processed_data[0]
        
        result = DataCleaning(processed_data, DataDivideStrategy()).handle_data()

        # Ensure the result is of the expected type
        if isinstance(result, tuple) and len(result) == 4:
            X_train, X_test, y_train, y_test = result
            logging.info("Data cleaning and splitting done successfully")
            return X_train, X_test, y_train, y_test
        else:
            raise TypeError("Unexpected return type from data spliting.")
        
    except Exception as e:
        logging.error(f"Error in cleaning and splitting data: {e}")
        raise e
        

