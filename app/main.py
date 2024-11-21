from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Grammar Correction API")

# Include routes
app.include_router(router)
