from pydantic import BaseModel
from typing import Optional, List

from DataIngestion.Models.BalanceSheetModel import BalanceSheet
from DataIngestion.Models.CashFlowStatementModel import CashFlow
from DataIngestion.Models.EnterpriseValuesModel import EnterpriseValues
from DataIngestion.Models.FinancialGrowthModel import FinancialGrowth
from DataIngestion.Models.FinancialRatiosModel import FinancialRatio
from DataIngestion.Models.IncomeStatementModel import IncomeStatement
from DataIngestion.Models.KeyMetricsModel import KeyMetric

class CompanyFinancials(BaseModel):
    income_statement: List[IncomeStatement]
    balance_sheet: List[BalanceSheet]
    cash_flow: List[CashFlow]
    financial_ratio: List[FinancialRatio]
    key_metrics: List[KeyMetric]
    financial_growth: List[FinancialGrowth]
    enterprise_values: List[EnterpriseValues]
