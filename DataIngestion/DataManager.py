import json
from typing import List, Callable, Optional
import psycopg2
import os
from datetime import datetime
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


    def _available_periods(self):
        today = datetime.today()
        month = today.month
        available = []

        # Determine current quarter
        if 1 <= month <= 3:
            available.append('Q1')
        if 4 <= month <= 6:
            available.append('Q2')
        if 7 <= month <= 9:
            available.append('Q3')
        if 10 <= month <= 12:
            available.append('Q4')

        # FY and annual always include everything up to now
        available.append('FY')
        available.append('quarter')

        return available

    def shutdown(self) -> None:
        self.cur.close()
        self.conn.close()

    async def get_company_data_with_error_handling(self, func: Callable, company: str, period: int) -> Optional[dict]:
        try:
            return await func(company, period, limit=1)
        except Exception as e:
            print(f"Ingestion error: {type(e).__name__}: {e}")
            return None
    
    async def get_current_year_market_data(self):
        periods = self._available_periods()
        market_data = {}
        for company in self.companies:
            years_data = {}
            period_data = {}

            for period in periods:
                income_statement = await self.get_company_data_with_error_handling(
                    self.market_ingestor.get_income_statement, 
                    company, 
                    period 
                )
                balance_sheet = await self.get_company_data_with_error_handling(self.market_ingestor.get_balance_sheet_statement, company, period)
                cash_flow = await self.get_company_data_with_error_handling(self.market_ingestor.get_cash_flow_statement, company, period)
                financial_ratio = await self.get_company_data_with_error_handling(self.market_ingestor.get_financial_ratios, company, period)
                key_metrics = await self.get_company_data_with_error_handling(self.market_ingestor.get_key_metrics, company, period)
                financial_growth = await self.get_company_data_with_error_handling(self.market_ingestor.get_financial_growth, company, period)
                enterprise_values = await self.get_company_data_with_error_handling(self.market_ingestor.get_enterprise_values, company, period)
                
                period_data[period] = {
                    "income_statement": income_statement,
                    "balance_sheet": balance_sheet,
                    "cash_flow": cash_flow,
                    "financial_ratio": financial_ratio,
                    "key_metrics": key_metrics,
                    "financial_growth": financial_growth,
                    "enterprise_values": enterprise_values,
                }
            years_data[datetime.now().year] = period_data
            market_data[company] = years_data
        return market_data


    async def ingest_data(self):
        market_data = await self.get_current_year_market_data()
        with open("output.txt", "w") as f:
            json.dump(market_data, f, indent=2)
        print(market_data)
        
        return