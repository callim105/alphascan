import requests
import pandas as pd
from util.api_util import AV_API_KEY

def daily_adjusted_ohlc(symbol):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&outputsize=full&apikey={AV_API_KEY}"
    r = requests.get(url)
    data = r.json()
    df = pd.DataFrame(data[f"Time Series (Daily)"]).T
    df = df.rename(
        columns={
            '1. open': 'open',
            '2. high': 'high', 
            '3. low': 'low', 
            '4. close': 'close',
            '5. adjusted close': 'adj_close', 
            '6. volume': 'volume',
            '7. dividend amount': 'dividend',
            '8. split coefficient': 'split_coefficient'
    })
    df.index = pd.to_datetime(df.index)
    df[df.columns] = df[df.columns].astype("float64")
    df['symbol'] = symbol
    return df