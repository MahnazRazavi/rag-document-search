from app.core.dependencies import (
    get_chat_service,
)
from app.schemas.chat import (
    ChatRequest,
    ChatResponse,
    Source,
)
from fastapi import APIRouter

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post(
    "",
    response_model=ChatResponse,
)
def chat(
    request: ChatRequest,
):
    service = get_chat_service()

    answer, results = service.chat(
        question=request.question,
        top_k=request.top_k,
        document_id=request.document_id,
    )

    sources = []

    for result in results:
        payload = result.payload or {}

        sources.append(
            Source(
                chunk_id=payload["chunk_id"],
                document_id=payload["document_id"],
                chunk_index=payload["chunk_index"],
                text=payload["text"],
                score=result.score,
            )
        )

    return ChatResponse(
        answer=answer,
        sources=sources,
    )
