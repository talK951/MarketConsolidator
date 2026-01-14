from pydantic import BaseModel
from typing import Optional, List

class FinancialGrowth(BaseModel):
    symbol: Optional[str]
    date: Optional[str]
    fiscalYear: Optional[str]
    period: Optional[str]
    reportedCurrency: Optional[str]

    revenueGrowth: Optional[float]
    grossProfitGrowth: Optional[float]
    ebitgrowth: Optional[float]
    operatingIncomeGrowth: Optional[float]
    netIncomeGrowth: Optional[float]

    epsgrowth: Optional[float]
    epsdilutedGrowth: Optional[float]

    weightedAverageSharesGrowth: Optional[float]
    weightedAverageSharesDilutedGrowth: Optional[float]

    dividendsPerShareGrowth: Optional[float]
    operatingCashFlowGrowth: Optional[float]
    receivablesGrowth: Optional[float]
    inventoryGrowth: Optional[float]
    assetGrowth: Optional[float]

    bookValueperShareGrowth: Optional[float]
    debtGrowth: Optional[float]
    rdexpenseGrowth: Optional[float]
    sgaexpensesGrowth: Optional[float]
    freeCashFlowGrowth: Optional[float]

    tenYRevenueGrowthPerShare: Optional[float]
    fiveYRevenueGrowthPerShare: Optional[float]
    threeYRevenueGrowthPerShare: Optional[float]

    tenYOperatingCFGrowthPerShare: Optional[float]
    fiveYOperatingCFGrowthPerShare: Optional[float]
    threeYOperatingCFGrowthPerShare: Optional[float]

    tenYNetIncomeGrowthPerShare: Optional[float]
    fiveYNetIncomeGrowthPerShare: Optional[float]
    threeYNetIncomeGrowthPerShare: Optional[float]

    tenYShareholdersEquityGrowthPerShare: Optional[float]
    fiveYShareholdersEquityGrowthPerShare: Optional[float]
    threeYShareholdersEquityGrowthPerShare: Optional[float]

    tenYDividendperShareGrowthPerShare: Optional[float]
    fiveYDividendperShareGrowthPerShare: Optional[float]
    threeYDividendperShareGrowthPerShare: Optional[float]

    ebitdaGrowth: Optional[float]
    growthCapitalExpenditure: Optional[float]
    tenYBottomLineNetIncomeGrowthPerShare: Optional[float]
    fiveYBottomLineNetIncomeGrowthPerShare: Optional[float]
    threeYBottomLineNetIncomeGrowthPerShare: Optional[float]
