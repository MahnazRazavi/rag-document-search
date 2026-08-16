from app.core.config import settings
from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    PointStruct,
    VectorParams,
)


class QdrantService:
    def __init__(self):
        self.client = QdrantClient(
            host=settings.qdrant_host,
            port=settings.qdrant_port,
        )

        self.collection_name = settings.qdrant_collection

    def create_collection(self):
        collections = self.client.get_collections()

        exists = any(
            collection.name == self.collection_name
            for collection in collections.collections
        )

        if not exists:
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(
                    size=settings.embedding_dimension,
                    distance=Distance.COSINE,
                ),
            )

    def upsert(
        self,
        points: list[PointStruct],
    ):
        self.client.upsert(
            collection_name=self.collection_name,
            points=points,
        )

    def search(
        self,
        vector: list[float],
        limit: int = 5,
    ):
        return self.client.search(
            collection_name=self.collection_name,
            query_vector=vector,
            limit=limit,
        )
