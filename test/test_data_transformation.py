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