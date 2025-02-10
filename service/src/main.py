from fastapi import FastAPI
from src.api.court_process import router as court_process_router
from src.api.control_process import router as control_process_router

app = FastAPI()

app.include_router(court_process_router, prefix="/api", tags=["CourtProcess"])
app.include_router(control_process_router, prefix="/api", tags=["ControlProcess"])
