import requests
import pandas as pd
import numpy as np
from stock.lib.daily import daily_adjusted_ohlc
from stock.lib.intraday import intraday_ohlc
from stock.lib.technicals.indicators import sma, bbands
from stock.lib.fundamentals.company_info import * 
from stock.lib.fundamentals.earnings import *


def main():
    d = bbands("NVDA", "5min")
    print(d)


if __name__ == "__main__":
    main()

