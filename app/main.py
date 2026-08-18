from app.api.chat import router as chat_router
from app.api.documents import router as document_router
from fastapi import FastAPI

app = FastAPI(
    title="RAG Document Search",
)


app.include_router(document_router)

app.include_router(chat_router)
