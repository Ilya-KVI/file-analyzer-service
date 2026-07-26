from fastapi import APIRouter

from app.services.file_client import FileClient
from app.services.download_service import DownloadService

router = APIRouter()


@router.post("/download")
def download():

    client = FileClient(
        "http://91.199.149.128:18001",
        "ilya_kvi"
    )

    service = DownloadService(client)

    result = service.download_all_files()

    return result