from pydantic import BaseModel
from typing import Optional, List

class CashFlow(BaseModel):
    date: Optional[str]
    symbol: Optional[str]
    reportedCurrency: Optional[str]
    cik: Optional[str]
    filingDate: Optional[str]
    acceptedDate: Optional[str]
    fiscalYear: Optional[str]
    period: Optional[str]

    netIncome: Optional[int]
    depreciationAndAmortization: Optional[int]
    deferredIncomeTax: Optional[int]
    stockBasedCompensation: Optional[int]
    changeInWorkingCapital: Optional[int]

    accountsReceivables: Optional[int]
    inventory: Optional[int]
    accountsPayables: Optional[int]
    otherWorkingCapital: Optional[int]
    otherNonCashItems: Optional[int]

    netCashProvidedByOperatingActivities: Optional[int]

    investmentsInPropertyPlantAndEquipment: Optional[int]
    acquisitionsNet: Optional[int]
    purchasesOfInvestments: Optional[int]
    salesMaturitiesOfInvestments: Optional[int]
    otherInvestingActivities: Optional[int]
    netCashProvidedByInvestingActivities: Optional[int]

    netDebtIssuance: Optional[int]
    longTermNetDebtIssuance: Optional[int]
    shortTermNetDebtIssuance: Optional[int]

    netStockIssuance: Optional[int]
    netCommonStockIssuance: Optional[int]
    commonStockIssuance: Optional[int]
    commonStockRepurchased: Optional[int]
    netPreferredStockIssuance: Optional[int]

    netDividendsPaid: Optional[int]
    commonDividendsPaid: Optional[int]
    preferredDividendsPaid: Optional[int]

    otherFinancingActivities: Optional[int]
    netCashProvidedByFinancingActivities: Optional[int]

    effectOfForexChangesOnCash: Optional[int]
    netChangeInCash: Optional[int]

    cashAtEndOfPeriod: Optional[int]
    cashAtBeginningOfPeriod: Optional[int]

    operatingCashFlow: Optional[int]
    capitalExpenditure: Optional[int]
    freeCashFlow: Optional[int]

    incomeTaxesPaid: Optional[int]
    interestPaid: Optional[int]
