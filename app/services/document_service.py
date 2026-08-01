from app.models.document import Document, DocumentStatus
from app.models.document_chunk import DocumentChunk
from app.models.document_content import DocumentContent
from app.repositories.document_chunk_repository import DocumentChunkRepository
from app.repositories.document_content_repository import DocumentContentRepository
from app.repositories.document_repository import DocumentRepository
from app.services.chunking_service import ChunkingService
from app.services.pdf_extractor import PDFExtractor
from app.services.storage_service import StorageService


class DocumentService:
    def __init__(
        self,
        repository: DocumentRepository,
        content_repository: DocumentContentRepository,
        chunk_repository: DocumentChunkRepository,
        storage: StorageService,
        pdf_extractor: PDFExtractor,
        chunking_service: ChunkingService,
    ):
        self.repository = repository
        self.content_repository = content_repository
        self.chunk_repository = chunk_repository
        self.storage = storage
        self.pdf_extractor = pdf_extractor
        self.chunking_service = chunking_service

    def upload(self, uploaded_file):
        path = self.storage.save(uploaded_file)

        document = Document(
            filename=uploaded_file.filename,
            storage_path=path,
            mime_type=uploaded_file.content_type,
            size=uploaded_file.size or 0,
        )

        document = self.repository.create(document)

        try:
            document.status = DocumentStatus.PROCESSING
            self.repository.create(document)

            result = self.pdf_extractor.extract(path)

            content = DocumentContent(
                document_id=document.id,
                text=result["text"],
                page_count=result["page_count"],
            )

            self.content_repository.create(content)

            chunks_data = self.chunking_service.chunk_text(result["text"])

            chunks = [
                DocumentChunk(
                    document_id=document.id,
                    chunk_index=i,
                    text=chunk["text"],
                    token_count=chunk["token_count"],
                )
                for i, chunk in enumerate(chunks_data)
            ]

            if chunks:
                self.chunk_repository.bulk_create(chunks)

            document.status = DocumentStatus.INDEXED
            self.repository.create(document)

        except Exception:  # noqa: BLE001
            document.status = DocumentStatus.FAILED
            self.repository.create(document)

        return document
