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
    # Ingest data
    df = ingest_df(data_path)  # 1)
    
    # Clean and split data
    X_train, X_test, y_train, y_test = clean_df(df)  # 2)
    
    # Train model with training data
    model_path = train_model(X_train, y_train)  # 3)
    
    # Evaluate the model with test data
    metrics = evaluate_model(model_path, X_test, y_test)  # 4)

