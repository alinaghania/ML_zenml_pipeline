from zenml import pipeline 
from steps.ingest_data import ingest_df
from steps.clean_data import clean_df
from steps.model_train import train_model
from steps.evaluation import evaluate_model



@pipeline(enable_cache=True)
def train_pipeline(data_path: str):
    """
    Training pipeline for the model
    """
    
    df = ingest_df(data_path) # 1) 
    clean_df(df) # 2)
    train_model(df) # 3) 
    evaluate_model(df)      # 4) 