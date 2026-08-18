from functools import lru_cache

from app.services.chat_service import (
    ChatService,
)
from app.services.context_service import (
    ContextService,
)
from app.services.embedding_service import (
    get_embedding_service,
)
from app.services.llm_service import (
    LLMService,
)
from app.services.qdrant_service import (
    QdrantService,
)
from app.services.retrieval_service import (
    RetrievalService,
)


@lru_cache
def get_qdrant_service():
    return QdrantService()


@lru_cache
def get_llm_service():
    return LLMService()


@lru_cache
def get_context_service():
    return ContextService()


def get_retrieval_service():
    return RetrievalService(
        embedding_service=get_embedding_service(),
        qdrant_service=get_qdrant_service(),
    )


def get_chat_service():
    return ChatService(
        retrieval_service=get_retrieval_service(),
        context_service=get_context_service(),
        llm_service=get_llm_service(),
    )
