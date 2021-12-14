from stock.lib.fundamentals.company_info import query_av


def get_annual_earnings(symbol):
    df = query_av(function="EARNINGS", symbol=symbol, datatype="annualEarnings")
    return df


def get_quarterly_earnings(symbol):
    df = query_av(function="EARNINGS", symbol=symbol, datatype="quarterlyEarnings")
    return df 