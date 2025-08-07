import json
import pandas as pd

# for 6 aug 2025

# Load JSON from file
with open("data.json", "r") as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data["data"])

df['timestamp'] = pd.to_datetime(df['timestamp'])
df['minute'] = df['timestamp'].dt.floor('min')

ohlcv = df.groupby(['stockSymbol', 'minute']).agg(
    open_price=('rate', 'first'),
    high_price=('rate', 'max'),
    low_price=('rate', 'min'),
    close_price=('rate', 'last'),
    volume=('quantity', 'sum')
).reset_index()

print(ohlcv)
