import requests

class StockMarketDataIngestor:

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.url = "https://financialmodelingprep.com/stable/"

    def get_income_statement(self, symbol:str, period: str, limit: int):
        params = {
            "symbol": symbol,  # ticker
            "period": period,  # or "quarter"
            "limit": limit,  # number of periods
            "apikey": self.api_key,
        }

        resp = requests.get(self.url + "income-statement", params=params, timeout=10)
        resp.raise_for_status()
        return resp.json()

    def get_balance_sheet_statement(self, symbol: str, period: str, limit: int):
        params = {
            "symbol": symbol,  # ticker
            "period": period,  # or "quarter"
            "limit": limit,  # number of periods
            "apikey": self.api_key,
        }
        resp = requests.get(self.url + "balance-sheet-statement", params=params, timeout=10)
        resp.raise_for_status()
        return resp.json()

    def get_cash_flow_statement(self, symbol: str, period: str, limit: int):
        params = {
            "symbol": symbol,  # ticker
            "period": period,  # or "quarter"
            "limit": limit,  # number of periods
            "apikey": self.api_key,
        }
        resp = requests.get(self.url + "cash-flow-statement", params=params, timeout=10)
        resp.raise_for_status()
        return resp.json()



s = StockMarketDataIngestor("4NbGTYwyYmd6Wp5ELl4mhXEQXE6x6fFg")

print(s.get_cash_flow_statement("AAPL", "FY", 1))