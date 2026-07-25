from fastapi import FastAPI

app = FastAPI(
    title="RAG Document Search",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {"status": "running"}