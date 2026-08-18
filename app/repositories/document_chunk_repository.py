from app.models.document_chunk import DocumentChunk


class DocumentChunkRepository:
    def __init__(self, db):
        self.db = db

    def bulk_create(self, chunks: list[DocumentChunk]) -> list[DocumentChunk]:
        self.db.add_all(chunks)
        self.db.commit()
        for chunk in chunks:
            self.db.refresh(chunk)
        return chunks
