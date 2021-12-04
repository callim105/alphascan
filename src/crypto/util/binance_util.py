import logging
from typing import Dict, Optional
from binance.client import Client
from util.api_util import BINANCE_KEY, BINANCE_SECRET

class BinanceClient(Client):
    """
    Convenience wrapper around the python-binance Client
    so you don't have to manually provide api keys. Just setup
    the api in your .env files.
    """
    def __init__(self, 
                 api_key: Optional[str] = BINANCE_KEY, 
                 api_secret: Optional[str] = BINANCE_SECRET, 
                 requests_params: Dict[str, str] = None, 
                 tld: str = 'us', 
                 testnet: bool = False):
        super().__init__(api_key=api_key, api_secret=api_secret, requests_params=requests_params, tld=tld, testnet=testnet)
        try:
            self.get_account()
        except:
            logging.error("Invalid api key")
            return None
        logging.info("Client successfully connected.")

