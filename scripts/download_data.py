import yfinance as yf
import pandas as pd
import os

# Create data directory if it doesn't exist
os.makedirs('../data', exist_ok=True)

# Define the indices we want to download
indices = {
    'SP500': '^GSPC',
    'FTSE100': '^FTSE',
    'EuroStoxx50': '^STOXX50E',
    'Nikkei225': '^N225',
    'VIX': '^VIX'
}

# Download data from 2000 to 2020
start_date = '2000-01-01'
end_date = '2020-12-31'

print("Downloading stock market data...")

for name, ticker in indices.items():
    print(f"Downloading {name} ({ticker})...")
    
    
    data = yf.download(ticker, start=start_date, end=end_date)
    
   
    filename = f'../data/{name}.csv'
    data.to_csv(filename)
    print(f"Saved {name} to {filename}")

print("\nAll data downloaded successfully!")
print("\nFiles saved:")
for name in indices.keys():
    filepath = f'../data/{name}.csv'
    if os.path.exists(filepath):
        df = pd.read_csv(filepath)
        print(f"  {name}: {len(df)} rows")
