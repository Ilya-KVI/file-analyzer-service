from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates

from app.database import SessionLocal
from app.models.file import DownloadedFile
from app.services.statistics_service import StatisticsService


router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/files")
def files(
request: Request,
page: int = 1):

    db = SessionLocal()

    try:

        page_size = 50

        offset = (page - 1) * page_size

        files = (
            db.query(DownloadedFile)
            .order_by(
                DownloadedFile.downloaded_at.desc()
            )
            .offset(offset)
            .limit(page_size)
            .all()
        )

        total_files = (
            db.query(DownloadedFile)
            .count()
        )

        total_pages = (
            total_files + page_size - 1
        ) // page_size

        return templates.TemplateResponse(
            request=request,
            name="files.html",
            context={
                "request": request,
                "files": files,
                "page": page,
                "total_pages": total_pages
            }
        )

    finally:
        db.close()
