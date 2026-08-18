from uuid import UUID

from app.services.embedding_service import (
    EmbeddingService,
)
from app.services.qdrant_service import (
    QdrantService,
)


class RetrievalService:
    def __init__(
        self,
        embedding_service: EmbeddingService,
        qdrant_service: QdrantService,
    ):
        self.embedding_service = embedding_service
        self.qdrant_service = qdrant_service

    def retrieve(
        self,
        question: str,
        top_k: int = 5,
        document_id: UUID | None = None,
    ):
        query_vector = self.embedding_service.embed_text(question)

        return self.qdrant_service.search(
            vector=query_vector,
            limit=top_k,
            document_id=(str(document_id) if document_id else None),
        )
