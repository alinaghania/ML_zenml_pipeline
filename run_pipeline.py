from pipelines.training_pipeline import train_pipeline
import pandas as pd

# Run the pipeline

if __name__ == "__main__":
    train_pipeline(data_path='MLweather_pipeline/data/insurance.csv')