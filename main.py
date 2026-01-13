from fastapi import FastAPI
from dotenv import load_dotenv
import asyncio


from DataIngestion.DataManager import DataManager
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # ---------- STARTUP ----------
    load_dotenv()
    app.state.data_manager = DataManager()
    stop_event = asyncio.Event()

    async def _daily_ingest():
        while not stop_event.is_set():
            try:
                print("Running daily ingestion")
                await app.state.data_manager.ingest_data()  # async method preferred
            except Exception as e:
                print(f"Ingestion error: {e}")

            try:
                await asyncio.wait_for(stop_event.wait(), timeout=5)#24*60*60)
            except asyncio.TimeoutError as e:
                print(f"Wait error {e}")
    task = asyncio.create_task(_daily_ingest())

    try:
        print("STARTING")
        yield
    finally:
        # ---------- SHUTDOWN ----------
        stop_event.set()         # signal the loop to stop
        await task
        app.state.data_manager.shutdown()
        print("SHUTDOWN")


app = FastAPI(title="Company Value Dashboard", lifespan=lifespan)

@app.get("/")
def server_startup():
    return {"Status": "Project Startup successfully"}
