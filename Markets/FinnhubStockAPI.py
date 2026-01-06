import time
from typing import List

import requests

from Markets.MarketAPI import MarketAPI


class FinnhubStockAPI(MarketAPI):

    def __init__(self, api_key: str, stocks: List[str]):
        super().__init__(api_key, stocks)

    def _get_latest_price(self, symbol: str) -> float | None:
        url = "https://finnhub.io/api/v1/quote"
        params = {
            "symbol": symbol,
            "token": self.api_key
        }

        try:
            response = requests.get(url, params=params)
            data = response.json()

            # Finnhub returns:
            # c: current price
            # h: high price of the day
            # l: low price of the day
            # o: open price of the day
            # pc: previous close
            price = data.get("c")
            if price is None:
                return None

            return float(price)

        except Exception:
            # Handle network errors or JSON errors
            return None

    def get_market(self) -> dict:
        """
        Fetch prices for all stocks sequentially, adding a 1-second delay between calls.
        """
        results = []

        for stock in self.stocks:
            price = self._get_latest_price(stock)  # synchronous
            results.append((stock, price))

            # Wait 1 second to avoid rate limits
            time.sleep(1)

        for symbol, price in results:
            if symbol not in self.data:
                self.data[symbol] = [price]
            else:
                self.data[symbol].append(price)

        return self.data