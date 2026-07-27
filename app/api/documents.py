from app.db import get_db
from app.repositories.document_repository import DocumentRepository
from app.schemas.document import DocumentResponse
from app.services.document_service import DocumentService
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
    storage = StorageService()

    service = DocumentService(repository, storage)

    return service.upload(file)
