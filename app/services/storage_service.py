import shutil
import uuid
from pathlib import Path


class StorageService:
    STORAGE_DIR = Path("storage")

    def __init__(self):
        self.STORAGE_DIR.mkdir(exist_ok=True)

    def save(self, uploaded_file):
        extension = Path(uploaded_file.filename).suffix

        filename = f"{uuid.uuid4()}{extension}"

        destination = self.STORAGE_DIR / filename

        with destination.open("wb") as buffer:
            shutil.copyfileobj(uploaded_file.file, buffer)

        return str(destination)
