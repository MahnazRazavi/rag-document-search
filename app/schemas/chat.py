from uuid import UUID

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    question: str = Field(
        min_length=1,
        max_length=2000,
    )

    document_id: UUID | None = None

    top_k: int = Field(
        default=5,
        ge=1,
        le=20,
    )


class Source(BaseModel):
    chunk_id: UUID
    document_id: UUID
    chunk_index: int
    text: str
    score: float


class ChatResponse(BaseModel):
    answer: str
    sources: list[Source]
