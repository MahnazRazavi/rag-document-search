from app.api.documents import router as document_router
from fastapi import FastAPI

app = FastAPI()

app.include_router(document_router)
