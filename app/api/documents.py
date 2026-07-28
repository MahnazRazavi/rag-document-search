from app.db import get_db
from app.repositories.document_content_repository import DocumentContentRepository
from app.repositories.document_repository import DocumentRepository
from app.schemas.document import DocumentResponse
from app.services.document_service import DocumentService
from app.services.pdf_extractor import PDFExtractor
from app.services.storage_service import StorageService
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
    storage = StorageService()
    pdf_extractor = PDFExtractor()

    service = DocumentService(repository, content_repository, storage, pdf_extractor)

    return service.upload(file)
