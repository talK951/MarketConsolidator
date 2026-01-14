from pydantic import BaseModel
from typing import Optional, List

class IncomeStatement(BaseModel):
    date: Optional[str]
    symbol: Optional[str]
    reportedCurrency: Optional[str]
    cik: Optional[str]
    filingDate: Optional[str]
    acceptedDate: Optional[str]
    fiscalYear: Optional[str]
    period: Optional[str]

    revenue: Optional[int]
    costOfRevenue: Optional[int]
    grossProfit: Optional[int]

    researchAndDevelopmentExpenses: Optional[int]
    generalAndAdministrativeExpenses: Optional[int]
    sellingAndMarketingExpenses: Optional[int]
    sellingGeneralAndAdministrativeExpenses: Optional[int]
    otherExpenses: Optional[int]
    operatingExpenses: Optional[int]

    costAndExpenses: Optional[int]

    netInterestIncome: Optional[int]
    interestIncome: Optional[int]
    interestExpense: Optional[int]

    depreciationAndAmortization: Optional[int]
    ebitda: Optional[int]
    ebit: Optional[int]

    nonOperatingIncomeExcludingInterest: Optional[int]
    operatingIncome: Optional[int]
    totalOtherIncomeExpensesNet: Optional[int]

    incomeBeforeTax: Optional[int]
    incomeTaxExpense: Optional[int]

    netIncomeFromContinuingOperations: Optional[int]
    netIncomeFromDiscontinuedOperations: Optional[int]
    otherAdjustmentsToNetIncome: Optional[int]

    netIncome: Optional[int]
    netIncomeDeductions: Optional[int]
    bottomLineNetIncome: Optional[int]

    eps: Optional[float]
    epsDiluted: Optional[float]

    weightedAverageShsOut: Optional[int]
    weightedAverageShsOutDil: Optional[int]
