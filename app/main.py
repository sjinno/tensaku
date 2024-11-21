from fastapi import FastAPI
from app.routes import router
from mangum import Mangum

app = FastAPI(title="Grammar Correction API")

# Include routes
app.include_router(router)

# Add a Mangum adapter to handle AWS Lambda events
handler = Mangum(app, TEXT_MIME_TYPES=["application/json"])
