import argparse
from pipelines.training_pipeline import train_pipeline
import logging


def main(data_path):
    train_pipeline(data_path=data_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the ML training pipeline with new data.")
    parser.add_argument('data_path', type=str, help="Path to the data file.")
    
    args = parser.parse_args()
    main(data_path=args.data_path)
