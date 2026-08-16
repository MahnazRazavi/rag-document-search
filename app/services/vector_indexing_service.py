from app.services.embedding_service import (
    EmbeddingService,
)
from app.services.qdrant_service import QdrantService
from qdrant_client.models import PointStruct


class VectorIndexingService:
    def __init__(
        self,
        embedding_service: EmbeddingService,
        qdrant_service: QdrantService,
    ):
        self.embedding_service = embedding_service

        self.qdrant_service = qdrant_service

    def index_chunks(self, chunks):
        self.qdrant_service.create_collection()

        texts = [chunk.text for chunk in chunks]

        embeddings = self.embedding_service.embed_texts(texts)

        points = []

        for chunk, embedding in zip(
            chunks,
            embeddings,
        ):
            point = PointStruct(
                id=str(chunk.id),
                vector=embedding,
                payload={
                    "chunk_id": str(chunk.id),
                    "document_id": str(chunk.document_id),
                    "chunk_index": (chunk.chunk_index),
                    "text": chunk.text,
                },
            )

            points.append(point)

        self.qdrant_service.upsert(points)

        return len(points)
