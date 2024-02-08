from typing import Tuple, Annotated
from zenml import pipeline, step

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error


@step
def load_and_preprocess_data(dataset_filepath: str) -> pd.DataFrame:
    df = pd.read_csv(dataset_filepath, sep=';')
    df.fillna(method='ffill', inplace=True)
    df = df[['T', 'U', 'FF', 'RR1']]

    df.dropna(inplace=True)
    df.reset_index(drop=True, inplace=True)

    scaler = StandardScaler()
    df[['T', 'U', 'FF', 'RR1']] = scaler.fit_transform(df[['T', 'U', 'FF', 'RR1']])

    return df


@step
def feature_engineering(df: pd.DataFrame) -> Tuple[
    Annotated[pd.DataFrame, 'train_features'],
    Annotated[pd.DataFrame, 'test_features'],
    Annotated[pd.Series, 'train_labels'],
    Annotated[pd.Series, 'test_labels']
]:
    df['T_lag1'] = df['T'].shift(1)

    labels = df['T'].shift(-1)

    features = df.drop(['T'], axis=1)

    valid_indices = features.dropna().index.intersection(labels.dropna().index)
    features, labels = features.loc[valid_indices], labels.loc[valid_indices]

    train_features, test_features, train_labels, test_labels = train_test_split(
        features, labels, test_size=0.2, random_state=42)

    return train_features, test_features, train_labels, test_labels


@step
def train_and_evaluate_model(
    train_features: pd.DataFrame, test_features: pd.DataFrame, train_labels: pd.Series, test_labels: pd.Series
) -> None:
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(train_features, train_labels)

    # Evaluate the model
    predictions = model.predict(test_features)
    mse = mean_squared_error(test_labels, predictions)
    print(f"Test Mean Squared Error: {mse}")


@pipeline
def pipeline():
    df = load_and_preprocess_data(dataset_filepath='./data/raw/H_01_latest-2023-2024.csv')
    train_features, test_features, train_labels, test_labels = feature_engineering(df=df)
    train_and_evaluate_model(train_features=train_features, test_features=test_features,
                             train_labels=train_labels, test_labels=test_labels)
