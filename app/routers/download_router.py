from fastapi import APIRouter

from app.database import SessionLocal
from app.services.file_client import FileClient
from app.services.download_service import DownloadService
from app.services.file_storage_service import FileStorageService

router = APIRouter()


@router.post("/download")
def download():

    client = FileClient(
        "http://91.199.149.128:18001",
        "Ilya_kvi"
    )

    storage_service = FileStorageService()

    db = SessionLocal()

    try:

        service = DownloadService(
            client,
            storage_service,
            db
        )

        result = service.download_all_files()

        return result

    finally:
        db.close()