import logging 
import pandas as pd
from zenml import step
from typing_extensions import Annotated
from typing import Tuple

from src.data_cleaning import DataCleaning, DataDivideStrategy, DataPreProcessStrategy

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
    process_strategy = DataPreProcessStrategy()
    data_cleaning = DataCleaning(df, process_strategy)

    processed_data = data_cleaning.handle_data()
    if processed_data is None:
        raise Exception("Preprocessing of data failed.")

    divide_strategy = DataDivideStrategy()
    data_cleaning = DataCleaning(processed_data, divide_strategy)

    split_data = data_cleaning.handle_data()
    if split_data is None:
        raise Exception("Splitting of data failed.")
    X_train, X_test, y_train, y_test = split_data

    logging.info(f"Data cleaning and splitting done successfully")
    return X_train, X_test, y_train, y_test
