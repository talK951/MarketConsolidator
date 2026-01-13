from pydantic import BaseModel
from datetime import date, datetime

class BalanceSheetStatement(BaseModel):
    date: date
    symbol: str
    reportedCurrency: str
    cik: str
    filingDate: datetime
    acceptedDate: datetime
    fiscalYear: str
    period: str

    # Current Assets
    cashAndCashEquivalents: int
    shortTermInvestments: int
    cashAndShortTermInvestments: int
    netReceivables: int
    accountsReceivables: int
    otherReceivables: int
    inventory: int
    prepaids: int
    otherCurrentAssets: int
    totalCurrentAssets: int

    # Non-Current Assets
    propertyPlantEquipmentNet: int
    goodwill: int
    intangibleAssets: int
    goodwillAndIntangibleAssets: int
    longTermInvestments: int
    taxAssets: int
    otherNonCurrentAssets: int
    totalNonCurrentAssets: int
    otherAssets: int
    totalAssets: int

    # Current Liabilities
    totalPayables: int
    accountPayables: int
    otherPayables: int
    accruedExpenses: int
    shortTermDebt: int
    capitalLeaseObligationsCurrent: int
    taxPayables: int
    deferredRevenue: int
    otherCurrentLiabilities: int
    totalCurrentLiabilities: int

    # Non-Current Liabilities
    longTermDebt: int
    deferredRevenueNonCurrent: int
    deferredTaxLiabilitiesNonCurrent: int
    otherNonCurrentLiabilities: int
    totalNonCurrentLiabilities: int
    otherLiabilities: int
    capitalLeaseObligations: int
    totalLiabilities: int

    # Stockholders' Equity
    treasuryStock: int
    preferredStock: int
    commonStock: int
    retainedEarnings: int
    additionalPaidInCapital: int
    accumulatedOtherComprehensiveIncomeLoss: int
    otherTotalStockholdersEquity: int
    totalStockholdersEquity: int
    totalEquity: int
    minorityInterest: int
    totalLiabilitiesAndTotalEquity: int

    # Other metrics
    totalInvestments: int
    totalDebt: int
    netDebt: int
