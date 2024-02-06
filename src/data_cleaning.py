import logging
from abc import ABC, abstractmethod 
from typing import Union
import numpy as np 
import pandas as pd
from sklearn.preprocessing import LabelEncoder 
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
            encod = LabelEncoder()

            # Encoding label column 
        
            data['sex'] = encod.fit_transform(data['sex'])
            data['smoker'] = encod.fit_transform(data['smoker'])
            
            # One hot encoding for region column

            data = pd.get_dummies(data,columns=['region'],prefix='region')
            data['region_northeast'] = data['region_northeast'].astype(int)
            data['region_northwest'] = data['region_northwest'].astype(int)
            data['region_southeast'] = data['region_southeast'].astype(int)
            data['region_southwest'] = data['region_southwest'].astype(int)

            # Dropping less correlated columns ( cf matrix correlation)
            y = data['charges'] # target column
            x = data.drop(columns=['charges','region_northwest','region_southwest','region_northeast','region_southeast','sex','children'])
                        


            X_train, X_test, y_train, y_test = train_test_split(

                x,
                y, 
                test_size=0.2,
                random_state=0

            )
            
