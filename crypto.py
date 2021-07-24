import pandas as pd


import os

main_df = pd.DataFrane()

ratios = ["BTC-USD", "LTC-USD", "ETH-USD", "BCH-USD"]

for ratio in ratios:
  dataset = f"crypto_data/{ratio}.csv"

  df = pd.read_csv(dataset, names=['time', 'low', 'high', 'open', 'close', 'volume'])  # read in specific file
  print(df.head())