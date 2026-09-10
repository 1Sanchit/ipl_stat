import pandas as pd
import os


BASE_PATH = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)


def load_data():

    matches = pd.read_csv(
        os.path.join(BASE_PATH, "data", "matches.csv")
    )

    deliveries = pd.read_csv(
        os.path.join(BASE_PATH, "data", "deliveries.csv")
    )

    return matches, deliveries



def load_deliveries():

    return pd.read_csv(
        os.path.join(BASE_PATH, "data", "deliveries.csv")
    )



def load_matches():

    return pd.read_csv(
        os.path.join(BASE_PATH, "data", "matches.csv")
    )