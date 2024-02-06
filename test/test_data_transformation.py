import pytest
import pandas as pd
from ..src.data_cleaning import DataPreProcessStrategy, DataDivideStrategy


class TestDataTransformation():
    def test_clean_data(self):
        # Init testing variable
        clean_data = DataPreProcessStrategy()
        df_test = pd.DataFrame(data=[
                [19,"female",27.9,0,"yes","southwest",16884.924],
                [18,"male",33.77,1,"no","southeast",1725.5523],
                [28,"male",33,3,"no","southeast",4449.462]
            ],
            columns=["age","sex","bmi","children","smoker","region","charges"])
        
        df_test = clean_data.handle_data(df_test)
        
        assert df_test.equals(pd.DataFrame(data=[
                [19,27.9,1,16884.924],
                [18,33.77,0,1725.5523],
                [28,33,0,4449.462]
            ],
            columns=["age","bmi","smoker","charges"]))
        
    def test_split_data(self):
        # Init testing variable
        split_data = DataDivideStrategy()
        df_test = pd.DataFrame(data=[
                [19,27.90,1,16884.9240],
                [18,33.77,0,1725.5523],
                [28,33.00,0,4449.4620]
            ],
            columns=["age",	"bmi", "smoker", "charges"])

        X_train, X_test, y_train, y_test = split_data.handle_data(df_test)

        assert X_train.equals(pd.DataFrame(data=[
                [0,	18,	33.77],
                [0,	28,	33.00]
            ],
            columns=["smoker","age","bmi"],
            index=[1, 2]))

        assert y_train.equals(pd.Series(
                data=[1725.5523, 4449.4620],
                index=[1, 2]
            ))
        
        assert X_test.equals(pd.DataFrame(data=[
                [1,	19,	27.9]
            ],
            columns=["smoker","age","bmi"]))

        assert y_test.equals(pd.Series(
                [16884.924]
        ))