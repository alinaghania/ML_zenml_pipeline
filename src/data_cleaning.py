import logging
from abc import ABC, abstractmethod 
from typing import Union
import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split


class DataStrategy(ABC):
    """
    Abstract class for handling data
    """
    @abstractmethod
    def handle_data(self, data: pd.DataFrame) -> Union[pd.DataFrame,pd.Series]:
        pass

class CleanData(DataStrategy):
    """
    Class for cleaning data
    """
    def handle_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Preprocess data
        """
        try:
            data = data.drop(
                [

                ],
                axis=1 
            )
            data = data.dropna() # Drop missing values