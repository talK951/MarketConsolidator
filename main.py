from fastapi import FastAPI

app = FastAPI(title="Market Consolidator")

@app.get("/")
def startup_verification():
    return {"Status": "Project Startup successfully"}

