import logging
from abc import ABC, abstractmethod 
from typing import Union
import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder



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
            
            data = data.dropna() # Drop missing values
            encoder = OneHotEncoder(sparse=False)
            X_encoded = encoder.fit_transform(data[['MONTH']])
            X_encoded = pd.DataFrame(X_encoded, columns=encoder.get_feature_names_out(['MONTH']))

            
            X_encoded = pd.concat((X_encoded, data.drop(columns=['MONTH'])), axis=1)
            X_encoded = X_encoded.drop(columns = 'BASEL_temp_min')
