import json
import logging
import pandas as pd
from crypto.util.binance_util import BinanceClient

def get_all_coins(client=None):
    """
    Returns a dataframe of all available coins on Binance.US
    """

    if client is None:
        logging.info("No binance client found, attempting to establish connection.")
        client = BinanceClient()

    
    coins = client.get_all_tickers()
    coins_df = pd.DataFrame(coins)
    if len(coins_df) == 0:
        logging.error("No data returned from get_all_tickers call")

    return coins_df

def get_recent_trades(client=None, coin='BTCUSD'):
    if client is None:
        logging.info("No binance client found, attempting to establish connection.")
        client = BinanceClient()

    recent_trades = client.get_recent_trades(symbol=coin)
    df = pd.DataFrame(recent_trades)
    df['time'] = pd.to_datetime(df['time'], unit='ms')
    return df

