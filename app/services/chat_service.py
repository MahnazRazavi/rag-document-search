from uuid import UUID

from app.services.context_service import (
    ContextService,
)
from app.services.llm_service import (
    LLMService,
)
from app.services.retrieval_service import (
    RetrievalService,
)


class ChatService:
    def __init__(
        self,
        retrieval_service: RetrievalService,
        context_service: ContextService,
        llm_service: LLMService,
    ):
        self.retrieval_service = retrieval_service
        self.context_service = context_service
        self.llm_service = llm_service

    def chat(
        self,
        question: str,
        top_k: int = 5,
        document_id: UUID | None = None,
    ):
        results = self.retrieval_service.retrieve(
            question=question,
            top_k=top_k,
            document_id=document_id,
        )

        context = self.context_service.build_context(results)

        answer = self.llm_service.generate(
            question=question,
            context=context,
        )

        return answer, results
