import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parents[2]   # go back to project root
RAW_PATH = BASE / "data" / "raw" / "Kaggle_market_csv"
PROCESSED_PATH = BASE / "data" / "processed"
PROCESSED_PATH.mkdir(parents=True, exist_ok=True)

def load_kaggle():
    df_meta = pd.read_csv(RAW_PATH / "symbols_valid_meta.csv")
    df_meta.columns = df_meta.columns.str.lower()
    df_meta.to_parquet(PROCESSED_PATH / "kaggle_metadata.parquet", index=False)

    df_prices = pd.read_csv(RAW_PATH / "WIKI_PRICES.csv", parse_dates=["date"], low_memory=False)
    df_prices.columns = df_prices.columns.str.lower()
    df_prices = df_prices.rename(columns={"ticker": "symbol"})
    df_prices = df_prices[["date","symbol","open","high","low","close","volume"]]

    df_prices.to_parquet(PROCESSED_PATH / "kaggle_prices_clean.parquet", index=False)
    print("Kaggle ETL complete.")

if __name__ == "__main__":
    load_kaggle()
