from pydantic import BaseModel
from typing import Optional, List


class BalanceSheet(BaseModel):
    date: Optional[str]
    symbol: Optional[str]
    reportedCurrency: Optional[str]
    cik: Optional[str]
    filingDate: Optional[str]
    acceptedDate: Optional[str]
    fiscalYear: Optional[str]
    period: Optional[str]

    cashAndCashEquivalents: Optional[int]
    shortTermInvestments: Optional[int]
    cashAndShortTermInvestments: Optional[int]

    netReceivables: Optional[int]
    accountsReceivables: Optional[int]
    otherReceivables: Optional[int]

    inventory: Optional[int]
    prepaids: Optional[int]
    otherCurrentAssets: Optional[int]
    totalCurrentAssets: Optional[int]

    propertyPlantEquipmentNet: Optional[int]
    goodwill: Optional[int]
    intangibleAssets: Optional[int]
    goodwillAndIntangibleAssets: Optional[int]

    longTermInvestments: Optional[int]
    taxAssets: Optional[int]
    otherNonCurrentAssets: Optional[int]
    totalNonCurrentAssets: Optional[int]
    otherAssets: Optional[int]

    totalAssets: Optional[int]

    totalPayables: Optional[int]
    accountPayables: Optional[int]
    otherPayables: Optional[int]
    accruedExpenses: Optional[int]

    shortTermDebt: Optional[int]
    capitalLeaseObligationsCurrent: Optional[int]
    taxPayables: Optional[int]
    deferredRevenue: Optional[int]
    otherCurrentLiabilities: Optional[int]
    totalCurrentLiabilities: Optional[int]

    longTermDebt: Optional[int]
    deferredRevenueNonCurrent: Optional[int]
    deferredTaxLiabilitiesNonCurrent: Optional[int]
    otherNonCurrentLiabilities: Optional[int]
    totalNonCurrentLiabilities: Optional[int]
    otherLiabilities: Optional[int]

    capitalLeaseObligations: Optional[int]
    totalLiabilities: Optional[int]

    treasuryStock: Optional[int]
    preferredStock: Optional[int]
    commonStock: Optional[int]
    retainedEarnings: Optional[int]
    additionalPaidInCapital: Optional[int]
    accumulatedOtherComprehensiveIncomeLoss: Optional[int]
    otherTotalStockholdersEquity: Optional[int]

    totalStockholdersEquity: Optional[int]
    totalEquity: Optional[int]
    minorityInterest: Optional[int]

    totalLiabilitiesAndTotalEquity: Optional[int]
    totalInvestments: Optional[int]
    totalDebt: Optional[int]
    netDebt: Optional[int]
