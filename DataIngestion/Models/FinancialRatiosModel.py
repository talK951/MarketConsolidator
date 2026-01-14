from pydantic import BaseModel
from typing import Optional, List

class FinancialRatio(BaseModel):
    symbol: Optional[str]
    date: Optional[str]
    fiscalYear: Optional[str]
    period: Optional[str]
    reportedCurrency: Optional[str]

    grossProfitMargin: Optional[float]
    ebitMargin: Optional[float]
    ebitdaMargin: Optional[float]
    operatingProfitMargin: Optional[float]
    pretaxProfitMargin: Optional[float]
    continuousOperationsProfitMargin: Optional[float]
    netProfitMargin: Optional[float]
    bottomLineProfitMargin: Optional[float]

    receivablesTurnover: Optional[float]
    payablesTurnover: Optional[float]
    inventoryTurnover: Optional[float]
    fixedAssetTurnover: Optional[float]
    assetTurnover: Optional[float]

    currentRatio: Optional[float]
    quickRatio: Optional[float]
    solvencyRatio: Optional[float]
    cashRatio: Optional[float]

    priceToEarningsRatio: Optional[float]
    priceToEarningsGrowthRatio: Optional[float]
    forwardPriceToEarningsGrowthRatio: Optional[float]
    priceToBookRatio: Optional[float]
    priceToSalesRatio: Optional[float]
    priceToFreeCashFlowRatio: Optional[float]
    priceToOperatingCashFlowRatio: Optional[float]

    debtToAssetsRatio: Optional[float]
    debtToEquityRatio: Optional[float]
    debtToCapitalRatio: Optional[float]
    longTermDebtToCapitalRatio: Optional[float]
    financialLeverageRatio: Optional[float]

    workingCapitalTurnoverRatio: Optional[float]

    operatingCashFlowRatio: Optional[float]
    operatingCashFlowSalesRatio: Optional[float]
    freeCashFlowOperatingCashFlowRatio: Optional[float]

    debtServiceCoverageRatio: Optional[float]
    interestCoverageRatio: Optional[float]
    shortTermOperatingCashFlowCoverageRatio: Optional[float]
    operatingCashFlowCoverageRatio: Optional[float]
    capitalExpenditureCoverageRatio: Optional[float]
    dividendPaidAndCapexCoverageRatio: Optional[float]

    dividendPayoutRatio: Optional[float]
    dividendYield: Optional[float]
    dividendYieldPercentage: Optional[float]

    revenuePerShare: Optional[float]
    netIncomePerShare: Optional[float]
    interestDebtPerShare: Optional[float]
    cashPerShare: Optional[float]
    bookValuePerShare: Optional[float]
    tangibleBookValuePerShare: Optional[float]
    shareholdersEquityPerShare: Optional[float]
    operatingCashFlowPerShare: Optional[float]
    capexPerShare: Optional[float]
    freeCashFlowPerShare: Optional[float]

    netIncomePerEBT: Optional[float]
    ebtPerEbit: Optional[float]
    priceToFairValue: Optional[float]
    debtToMarketCap: Optional[float]
    effectiveTaxRate: Optional[float]
    enterpriseValueMultiple: Optional[float]
