from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from app.database import engine
from app.database import Base

from app.models.file import DownloadedFile

from app.services.file_client import FileClient
from app.services.download_service import DownloadService
from app.routers.download_router import router as download_router

app = FastAPI(
    title="File Analyzer Service"
)

Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

app.include_router(download_router)

client = FileClient(
    base_url="http://91.199.149.128:18001",
    candidate_id="Ilya-KVI"
)

download_service = DownloadService(client)


@app.get("/")
def root(request: Request):
    context = {
        "request": request
    }

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context=context
    )