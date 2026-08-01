from app.models.document_chunk import DocumentChunk


class DocumentChunkService:
    def __init__(
        self,
        chunking_service,
        repository,
    ):
        self.chunking_service = chunking_service
        self.repository = repository

    def create_chunks(
        self,
        document_id,
        text,
    ):
        texts = self.chunking_service.split(text)

        chunks = []

        for index, chunk_text in enumerate(texts):
            chunk = DocumentChunk(
                document_id=document_id,
                chunk_index=index,
                text=chunk_text,
            )

            chunks.append(chunk)

        return self.repository.create_many(chunks)
