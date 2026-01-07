import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parents[2]
P = BASE / "data" / "processed"

kaggle_df = pd.read_parquet(P/"kaggle_prices_clean.parquet")
alpha_df = pd.read_parquet(P/"alpha_vantage_prices.parquet")

# Convert types
kaggle_df["date"] = pd.to_datetime(kaggle_df["date"])
alpha_df["date"] = pd.to_datetime(alpha_df["date"])

for c in ["open","high","low","close","volume"]:
    kaggle_df[c] = pd.to_numeric(kaggle_df[c], errors="coerce")
    alpha_df[c] = pd.to_numeric(alpha_df[c], errors="coerce")

# Merge
merged = pd.concat([kaggle_df, alpha_df])
merged = merged.sort_values(["symbol","date"])
merged = merged.drop_duplicates(["symbol","date"], keep="last")

merged.to_parquet(P/"market_data_merged.parquet", index=False)
print("Merged dataset created.")
