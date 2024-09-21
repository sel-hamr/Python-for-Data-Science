import pandas as pd
import os

def load(path: str) -> pd.DataFrame:
    try:
        if not path.lower().endswith(".csv"):
            raise AssertionError("The file fromat is not .csv")
        if not os.path.exists(path):
            raise("The file doesn't exist")
    except AssertionError as error:
        print(error)
    else:
      data = pd.read_csv(path)
      print(f"Loading dataset of dimension {data.shape}")
      return data
        