from app.models.document import Document, DocumentStatus
from app.models.document_content import DocumentContent
from app.repositories.document_content_repository import DocumentContentRepository
from app.repositories.document_repository import DocumentRepository
from app.services.pdf_extractor import PDFExtractor
from app.services.storage_service import StorageService


class DocumentService:
    def __init__(
        self,
        repository: DocumentRepository,
        content_repository: DocumentContentRepository,
        storage: StorageService,
        pdf_extractor: PDFExtractor,
    ):
        self.repository = repository
        self.content_repository = content_repository
        self.storage = storage
        self.pdf_extractor = pdf_extractor

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
            result = self.pdf_extractor.extract(path)

            content = DocumentContent(
                document_id=document.id,
                text=result["text"],
                page_count=result["page_count"],
            )

            self.content_repository.create(content)

            document.status = DocumentStatus.INDEXED
            self.repository.create(document)

        except Exception:  # noqa: BLE001
            document.status = DocumentStatus.FAILED
            self.repository.create(document)

        return document
