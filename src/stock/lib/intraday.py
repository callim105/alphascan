import requests
import pandas as pd
from util.api_util import AV_API_KEY

def intraday_ohlc(symbol, interval):
    """
    Returns dataframe of intraday ohlc values.

    interval opts: 1min, 5min, 15min, 30min, 60min

    """

    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}&apikey={AV_API_KEY}&outputsize=full"
    r = requests.get(url)
    data = r.json()

    df = pd.DataFrame(data[f"Time Series ({interval})"]).T
    df = df.rename(
        columns={
            '1. open': 'open',
            '2. high': 'high', 
            '3. low': 'low', 
            '4. close': 'close', 
            '5. volume': 'volume'
    })
    df.index = pd.to_datetime(df.index)
    df['symbol'] = symbol
    return df