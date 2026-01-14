from pydantic import BaseModel
from typing import Optional, List

class EnterpriseValues(BaseModel):
    symbol: Optional[str]
    date: Optional[str]
    stockPrice: Optional[float]
    numberOfShares: Optional[int]
    marketCapitalization: Optional[int]
    minusCashAndCashEquivalents: Optional[int]
    addTotalDebt: Optional[int]
    enterpriseValue: Optional[int]
