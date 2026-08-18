from app.services.embedding_service import (
    get_embedding_service,
)
from app.services.qdrant_service import (
    QdrantService,
)

embedding_service = get_embedding_service()
qdrant_service = QdrantService()


question = "What programming languages does the candidate know?"

vector = embedding_service.embed_text(question)

results = qdrant_service.search(
    vector=vector,
    limit=5,
)


for result in results:
    print(
        "Score:",
        result.score,
    )

    print(
        "Text:",
        result.payload.get("text"),
    )

    print("-" * 80)
