import requests
import pandas as pd
import time
from pathlib import Path

BASE = Path(__file__).resolve().parents[2]
PROCESSED_PATH = BASE / "data" / "processed"
PROCESSED_PATH.mkdir(parents=True, exist_ok=True)

API_KEY = "YOUR_KEY_HERE"  # replace

def fetch_alpha(symbol):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=compact&apikey={API_KEY}"
    r = requests.get(url).json()
    if "Time Series (Daily)" not in r:
        print(f"Error fetching {symbol}")
        return None
    df = pd.DataFrame(r["Time Series (Daily)"]).T
    df.index = pd.to_datetime(df.index)
    df.sort_index(inplace=True)
    df = df.rename(columns={
        "1. open": "open",
        "2. high": "high",
        "3. low": "low",
        "4. close": "close",
        "5. volume": "volume"
    })
    df = df.astype(float)
    df["symbol"] = symbol
    df = df.reset_index().rename(columns={"index": "date"})
    return df

def run_alpha(symbols):
    all_data = []
    for s in symbols:
        print("Fetching", s)
        df = fetch_alpha(s)
        if df is not None:
            all_data.append(df)
        time.sleep(12)
    if all_data: 
        out = pd.concat(all_data, ignore_index=True)
        out.to_parquet(PROCESSED_PATH / "alpha_vantage_prices.parquet", index=False)
        print("Alpha Vantage ETL complete.")

if __name__ == "__main__":
    symbols = ["AAPL","MSFT","AMZN","GOOGL","TSLA"]
    run_alpha(symbols)
