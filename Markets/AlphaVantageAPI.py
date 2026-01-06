import time
from typing import List

import requests

from Markets.MarketAPI import MarketAPI


class AlphaVantageAPI(MarketAPI):

    def __init__(self,  api_key:str, stocks: List[str]):
        super().__init__(api_key, stocks)

    def _get_latest_price(self, symbol: str) -> float | None:
        """
        Fetch the latest stock price using Alpha Vantage GLOBAL_QUOTE endpoint.
        Returns the current price as a float, or None if failed.
        """
        url = "https://www.alphavantage.co/query"
        params = {
            "function": "GLOBAL_QUOTE",
            "symbol": symbol,
            "apikey": self.api_key
        }

        try:
            response = requests.get(url, params=params)
            data = response.json()
            quote = data.get("Global Quote")
            if not quote:
                return symbol, None

            price = quote.get("05. price")
            if price is None:
                return None

            return float(price)

        except Exception as e:
            # Handle network errors on JSON errors
            return

    def get_market(self) -> dict:
        results = []
        for stock in self.stocks:
            price = self._get_latest_price(stock)  # synchronous
            results.append((stock, price))

            # half second
            time.sleep(1)

        for symbol, price in results:
            if symbol not in self.data:
                self.data[symbol] = [price]
            else:
                self.data[symbol].append(price)

        return self.data