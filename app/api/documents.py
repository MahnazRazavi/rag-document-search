from app.db import get_db
from app.repositories.document_chunk_repository import DocumentChunkRepository
from app.repositories.document_content_repository import DocumentContentRepository
from app.repositories.document_repository import DocumentRepository
from app.schemas.document import DocumentResponse
from app.services.chunking_service import ChunkingService
from app.services.document_service import DocumentService
from app.services.embedding_service import (
    get_embedding_service,
)
from app.services.pdf_extractor import PDFExtractor
from app.services.qdrant_service import QdrantService
from app.services.storage_service import StorageService
from app.services.vector_indexing_service import (
    VectorIndexingService,
)
from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.orm import Session

router = APIRouter(prefix="/documents", tags=["Documents"])

get_db_dependency = Depends(get_db)


@router.post("", response_model=DocumentResponse)
def upload_document(
    file: UploadFile,
    db: Session = get_db_dependency,
):
    repository = DocumentRepository(db)
    content_repository = DocumentContentRepository(db)
    chunk_repository = DocumentChunkRepository(db)
    storage = StorageService()
    pdf_extractor = PDFExtractor()
    chunking_service = ChunkingService()
    vector_indexing_service = VectorIndexingService(
        embedding_service=get_embedding_service(),
        qdrant_service=QdrantService(),
    )

    service = DocumentService(
        repository,
        content_repository,
        chunk_repository,
        storage,
        pdf_extractor,
        chunking_service,
        vector_indexing_service,
    )

    return service.upload(file)
