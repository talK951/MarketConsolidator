from typing import List


class MarketAPI:

    def __init__(self, api_key:str, stocks: List[str]):
        self.api_key = api_key
        self.stocks = stocks
        self.data = {}


    def IngestData(self) -> str:
        pass