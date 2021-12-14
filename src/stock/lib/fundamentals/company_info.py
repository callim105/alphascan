import requests
import pandas as pd
from util.api_util import AV_API_KEY


def query_av(function, symbol, datatype):
    url = f"https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={AV_API_KEY}"
    r = requests.get(url)
    req = r.json()
    symbol = req["symbol"]
    data = req[datatype]
    df = pd.DataFrame(data)
    df["symbol"] = symbol
    return df


def get_annual_income_statements(symbol):
    """
    Returns a dataframe of annual IS for the past 5 yrs.
    """
    df = query_av(function="INCOME_STATEMENT", symbol=symbol, datatype='annualReports')
    return df


def get_quarterly_income_statements(symbol):
    """
    Returns quarterly IS for the past 5 yrs.
    """
    df = query_av(function="INCOME_STATEMENT", symbol=symbol, datatype='quarterlyReports')
    return df


def get_annual_balance_sheets(symbol):
    """
    Returns annual balance sheet
    """
    df = query_av(function="BALANCE_SHEET", symbol=symbol, datatype="annualReports")
    return df


def get_quarterly_balance_sheets(symbol):
    df = query_av(function="BALANCE_SHEET", symbol=symbol, datatype="quarterlyReports")
    return df


def get_annual_cash_flows(symbol):
    """
    Returns a dataframe of annual cash flows for the past 5 yrs.
    """
    df = query_av(function="CASH_FLOW", symbol=symbol, datatype="annualReports")
    return df


def get_quarterly_cash_flows(symbol):
    """
    Returns quarterly cash flows for the past 5 yrs.
    """
    df = query_av(function="CASH_FLOW", symbol=symbol, datatype="quarterlyReports")
    return df


def company_info(symbol):
    """
    Returns a dict of company info
    """
    url = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={AV_API_KEY}"
    r = requests.get(url)
    req = r.json() 
    return req