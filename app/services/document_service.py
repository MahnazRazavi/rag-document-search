from app.models.document import Document
from app.repositories.document_repository import DocumentRepository
from app.services.storage_service import StorageService


class DocumentService:
    def __init__(
        self,
        repository: DocumentRepository,
        storage: StorageService,
    ):
        self.repository = repository
        self.storage = storage

    def upload(self, uploaded_file):
        path = self.storage.save(uploaded_file)

        document = Document(
            filename=uploaded_file.filename,
            storage_path=path,
            mime_type=uploaded_file.content_type,
            size=uploaded_file.size or 0,
        )

        return self.repository.create(document)
