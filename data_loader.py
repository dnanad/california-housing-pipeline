from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
import pandas as pd


def load_data():
    housing = fetch_california_housing()
    df = pd.DataFrame(housing.data, columns=housing.feature_names)
    df["MedHouseVal"] = housing.target

    # Split the dataset
    X = df.drop("MedHouseVal", axis=1)
    y = df["MedHouseVal"]
    return train_test_split(X, y, test_size=0.2, random_state=42)
