import requests
import pandas as pd
import numpy as np
from stock.daily import daily_adjusted_ohlc
from stock.intraday import intraday_ohlc
from stock.technicals.indicators import sma

def main():
    # js = intraday_ohlc(symbol="NVDA", interval="1min")
    js = daily_adjusted_ohlc("QRVO")
    s = sma("QRVO", "daily", 200, "close")
    df = js.join(s, how="inner", lsuffix='x')
    df.drop(inplace=True, columns=["Symbolx"])
    print(js)


if __name__ == "__main__":
    main()

