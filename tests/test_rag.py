from app.services.chat_service import ChatService
from app.services.context_service import ContextService
from app.services.embedding_service import get_embedding_service
from app.services.llm_service import LLMService
from app.services.qdrant_service import QdrantService
from app.services.retrieval_service import RetrievalService


def main():
    # 1. Initialize services

    embedding_service = get_embedding_service()

    qdrant_service = QdrantService()

    retrieval_service = RetrievalService(
        embedding_service=embedding_service,
        qdrant_service=qdrant_service,
    )

    context_service = ContextService()

    llm_service = LLMService()

    chat_service = ChatService(
        retrieval_service=retrieval_service,
        context_service=context_service,
        llm_service=llm_service,
    )

    # 2. Ask a question

    question = "What programming languages does the candidate know?"

    # 3. Run the complete RAG pipeline

    answer, results = chat_service.chat(
        question=question,
        top_k=5,
    )

    # 4. Print retrieved chunks

    print("\n" + "=" * 80)

    print("RETRIEVED CHUNKS")

    print("=" * 80)

    for i, result in enumerate(results):
        payload = result.payload or {}

        print(f"\n[{i + 1}] Score: {result.score:.4f}")

        print(payload.get("text", ""))

    # 5. Print final LLM answer

    print("\n" + "=" * 80)

    print("LLM ANSWER")

    print("=" * 80)

    print(answer)


if __name__ == "__main__":
    main()
