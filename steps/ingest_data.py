import logging  
import pandas as pd 
from zenml import step


class IngestData:
    """
    Class to read data from the data_path
    """
    def __init__(self, data_path: str): # data_path is the path to the data file to be read
        """
        Args: 
            data_path: Path to the data file to be read
        """
        self.data_path = data_path

    def get_data(self):
        logging.info(f"Reading data from {self.data_path}")
        return pd.read_csv(self.data_path)
    

@step
def ingest_df(data_path: str) -> pd.DataFrame:

    """
    Ingest data from the data_path
    
    Args:
        data_path: Path to the data file to be read
    Returns:    
        pd.DataFrame: The data read from the data_path
    """
    try:
        ingest_data = IngestData(data_path)
        df = ingest_data.get_data() # Read the data from the data_path
        return df
    except Exception as error:
        logging.error(f"Error reading data from {data_path}: {error}")
        raise error
    

