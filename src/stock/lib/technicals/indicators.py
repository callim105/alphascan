import requests
import pandas as pd
from util.api_util import AV_API_KEY


def sma(symbol, interval, time_period, series_type):
    """
    Returns a simple moving average

    Interval: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    Time_period: Number of datapoints used to calculate each moving avg value.
    """

    url = f"https://www.alphavantage.co/query?function=SMA&symbol={symbol}&interval={interval}&time_period={time_period}&series_type={series_type}&apikey={AV_API_KEY}"
    r = requests.get(url)
    data = r.json()
    metadata = data["Meta Data"]
    df = pd.DataFrame(data[f"Technical Analysis: SMA"]).T
    df.index = pd.to_datetime(df.index)
    df["SMA"] = df["SMA"].astype("float64")
    df = df.rename(columns={"SMA": f"SMA{time_period}"})
    df['symbol'] = symbol
    return df
