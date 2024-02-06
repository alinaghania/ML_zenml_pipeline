import logging
from abc import ABC, abstractmethod 
from typing import Union, Tuple
import pandas as pd
from sklearn.preprocessing import LabelEncoder 
from sklearn.model_selection import train_test_split


class DataStrategy(ABC):
    """
    Abstract class for handling data
    """
    @abstractmethod
    def handle_data(self, data: pd.DataFrame) -> Union[pd.DataFrame, pd.Series, Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series], None]:
        pass

class DataPreProcessStrategy(DataStrategy):
    """
    Class for cleaning data
    """
    def handle_data(self, data: pd.DataFrame) -> Union[pd.DataFrame, None]:
        """
        Preprocess data
        """
        try:
            encoder = LabelEncoder()

            # Encoding 'sex' and 'smoker' columns
            data['sex'] = encoder.fit_transform(data['sex'])
            data['smoker'] = encoder.fit_transform(data['smoker'])
            
            # One hot encoding for 'region' column
            data = pd.get_dummies(data, columns=['region'], prefix='region')

            # Dropping less correlated columns based on the correlation matrix
            data = data.drop(
                ['region_southeast', 'region_southwest', 'region_northeast', 'region_northwest', 'children', 'sex'],
                axis=1
            )

            return data
        except Exception as e:
            logging.error(f"Error in cleaning data: {e}")
            return None
        
class DataDivideStrategy(DataStrategy):
    """
    Split the data into train and test sets
    """
    def handle_data(self, data: pd.DataFrame) -> Union[Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series], None]:
        """
        Split the data into training and test sets and return them.
        """
        try:
            y = data['charges']  # Target column
            X = data.drop(['charges'], axis=1)  # Features, assuming 'charges' is the only target
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            return X_train, X_test, y_train, y_test
        except Exception as e:
            logging.error(f"Error in splitting data: {e}")
            return None

class DataCleaning:
    """
    Class to clean and split the data
    """
    def __init__(self, data: pd.DataFrame, strategy: DataStrategy):
        self.data = data
        self.strategy = strategy

    def handle_data(self) -> Union[pd.DataFrame, pd.Series, Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series], None]:
        """
        Clean the data
        """
        try:
            return self.strategy.handle_data(self.data)
        except Exception as e:  
            logging.error(f"Error in cleaning data: {e}")
            return None
