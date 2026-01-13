from typing import List
import psycopg2
import os

from .StockMarketDataIngestor import StockMarketDataIngestor


class DataManager:

    def __init__(self) -> None:
        self.conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            dbname=os.getenv("DB_NAME")
        ) 
        self.cur = self.conn.cursor()
        self.companies = os.getenv("COMPANIES","").split(",")
        self.market_ingestor = StockMarketDataIngestor(api_key=os.getenv("fmpAPI_Key"))

    def shutdown(self) -> None:
        self.cur.close()
        self.conn.close()

    async def get_market_data(self):
        market_data = {}
        for company in self.companies:
            market_data[company] = await self.market_ingestor.get_balance_sheet_statement(company, 'FY', 1)
        print(f"market_data= {market_data}")
        return market_data

    async def ingest_data(self):
        market_data = await self.get_market_data()
        self.save_market_data(market_data)
        return