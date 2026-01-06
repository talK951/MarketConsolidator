from fastapi import FastAPI
from Markets import AlphaVantageAPI, FinnhubStockAPI, MassiveAPI

markets = [AlphaVantageAPI(), FinnhubStockAPI(), MassiveAPI()]

app = FastAPI(title="Market Consolidator")

@app.get("/")
def startup_verification():
    return {"Status": "Project Startup successfully"}

@app.get("/Market/fetchMarketData")
def fetch_market_data():
    pass