import pandas as pd

data = pd.read_csv("risk-tribe/transactions_raw.csv")

data["timestamp"] = pd.to_datetime(data["timestamp"])

print(f"Number of records in the dataset: {data.shape[0]}")
print(f"Number of missing values: {data.isna().sum().sum()}")
