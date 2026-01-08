from typing import Optional

import requests

class StockMarketDataIngestor:

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.url = "https://financialmodelingprep.com/stable/"

    # -------------------------
    # Internal helper
    # -------------------------
    def _get(self, endpoint: str, params: dict):
        params["apikey"] = self.api_key
        resp = requests.get(self.url + endpoint, params=params, timeout=10)
        resp.raise_for_status()
        return resp.json()

    # -------------------------
    # Financial Statements
    # -------------------------
    def get_income_statement(self, symbol: str, period: str, limit: int):
        return self._get(
            "income-statement",
            {"symbol": symbol, "period": period, "limit": limit},
        )

    def get_balance_sheet_statement(self, symbol: str, period: str, limit: int):
        return self._get(
            "balance-sheet-statement",
            {"symbol": symbol, "period": period, "limit": limit},
        )

    def get_cash_flow_statement(self, symbol: str, period: str, limit: int):
        return self._get(
            "cash-flow-statement",
            {"symbol": symbol, "period": period, "limit": limit},
        )

    # -------------------------
    # Financial Ratios
    # -------------------------
    def get_financial_ratios(self, symbol: str, period: str, limit: int):
        """
        Liquidity, profitability, efficiency, leverage ratios:
        - Current ratio
        - ROE / ROA
        - Gross / operating / net margins
        - Debt ratios
        """
        return self._get(
            "ratios",
            {"symbol": symbol, "period": period, "limit": limit},
        )

    # -------------------------
    # Key Metrics
    # -------------------------
    def get_key_metrics(self, symbol: str, period: str, limit: int):
        """
        High-signal metrics for dashboards:
        - EPS, book value per share
        - Free cash flow per share
        - ROIC, ROE
        - Revenue per share
        """
        return self._get(
            "key-metrics",
            {"symbol": symbol, "period": period, "limit": limit},
        )

    # -------------------------
    # Growth Metrics
    # -------------------------
    def get_financial_growth(self, symbol: str, period: str, limit: int):
        """
        Growth rates:
        - Revenue growth
        - EPS growth
        - FCF growth
        - Net income growth
        """
        return self._get(
            "financial-growth",
            {"symbol": symbol, "period": period, "limit": limit},
        )

    # -------------------------
    # Valuation & Enterprise Value
    # -------------------------
    def get_enterprise_values(self, symbol: str, period: str, limit: int):
        """
        Enterprise value & valuation multiples:
        - EV
        - EV / EBITDA
        - EV / Revenue
        """
        return self._get(
            "enterprise-values",
            {"symbol": symbol, "period": period, "limit": limit},
        )

    # -------------------------
    # Market Data
    # -------------------------
    def get_quote(self, symbol: str):
        """
        Real-time-ish market snapshot:
        - Price
        - Market cap
        - PE
        - EPS
        - Volume
        """
        return self._get(
            "quote",
            {"symbol": symbol},
        )

    def get_company_profile(self, symbol: str):
        """
        Static company info:
        - Sector
        - Industry
        - Description
        - Beta
        - Market cap
        """
        return self._get(
            "profile",
            {"symbol": symbol},
        )

    # -------------------------
    # Historical Price Data (Chart API)
    # -------------------------
    def get_historical_price_chart(
            self,
            symbol: str,
            timeframe: str,
            from_date: Optional[str] = None,
            to_date: Optional[str] = None,
    ):
        """
        timeframe examples:
        - 1min, 5min, 15min, 1hour
        - 1day, 1week, 1month
        """
        params = {"symbol": symbol}

        if from_date:
            params["from"] = from_date
        if to_date:
            params["to"] = to_date

        return self._get(f"chart/{timeframe}", params)