import requests
import pandas as pd
from util.api_util import AV_API_KEY


def sma(symbol, interval, time_period=20, series_type='close'):
    """
    Returns a simple moving average

    Interval: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    Time_period: Number of datapoints used to calculate each moving avg value.
    series_type: The desired price type in the time series. Four supported: close, open, high, low
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


def bbands(symbol, interval, series_type='close', time_period=20, std_dev_up=2, std_dev_down=2, matype=0):
    """
    Returns bollinger bands 
    Goes back 25 days (cal days)

    Interval: Time interval between consecutive data points in the time series.
    - 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly

    time_period: The number of datapoints used to calculat each bbands value


    """
    url = f"https://www.alphavantage.co/query?function=BBANDS&symbol={symbol}&interval={interval}&time_period={time_period}&series_type={series_type}&nbdevup={std_dev_up}&nbdevdn={std_dev_down}&apikey={AV_API_KEY}"
    r = requests.get(url)
    data = r.json()
    bb = data["Technical Analysis: BBANDS"]
    df = pd.DataFrame(bb).T
    df = df.rename(columns={
        "Real Upper Band": "upper_bound",
        "Real Lower Band": "lower_bound",
        "Real Middle Band": "mid_bb"
    })
    df["symbol"] = symbol
    return df


