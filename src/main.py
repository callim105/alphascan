import requests
import pandas as pd
import numpy as np
from stock.lib.daily import daily_adjusted_ohlc
from stock.lib.intraday import intraday_ohlc
from stock.lib.technicals.indicators import sma
from stock.lib.fundamentals.company_info import * 
from stock.lib.fundamentals.earnings import *


def main():
    # js = intraday_ohlc(symbol="NVDA", interval="1min")
    # js = daily_adjusted_ohlc("QRVO")
    # s = sma("QRVO", "daily", 200, "close")
    # df = js.join(s, how="inner", lsuffix='x')
    # df.drop(inplace=True, columns=["Symbolx"])
    # print(js)
    # client = BinanceClient()
    # df = get_all_coins(client)
    # sol = get_coin_info(client, coin='SOLUSD')
    # print(df)
    # df = get_annual_income_statements('NVDA')
    # earn = get_quarterly_earnings("NVDA")
    info = company_info("NVDA")
    print(df)


if __name__ == "__main__":
    main()

