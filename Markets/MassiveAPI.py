import time
from typing import List

import requests

from Markets.MarketAPI import MarketAPI


class MassiveAPI(MarketAPI):

    def __init__(self, api_key: str, stocks: List[str]):
        super().__init__(api_key, stocks)

    def _get_latest_price(self, symbol: str) -> float | None:
        """
        Fetch the latest stock price for a single symbol from MassiveAPI.
        """
        url = f"https://api.massive.com/v2/snapshot/locale/us/markets/stocks/tickers/{symbol}"  # replace with actual endpoint
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json",
        }

        try:
            response = requests.get(url, headers=headers)
            data = response.json()
            print(data)

            # Assuming MassiveAPI returns a 'current_price' field
            price = data.get("current_price")
            if price is None:
                return None

            return float(price)

        except Exception:
            # Handle network errors or JSON parse errors
            return None

    def get_market(self) -> dict:
        """
        Fetch prices for all stocks sequentially, adding a 1-second delay between calls.
        """
        results = []

        for stock in self.stocks:
            price = self._get_latest_price(stock)
            results.append((stock, price))

            # Wait 1 second between requests to avoid rate limits
            time.sleep(1)

        # Update self.data
        for symbol, price in results:
            if symbol not in self.data:
                self.data[symbol] = [price]
            else:
                self.data[symbol].append(price)

        return self.data