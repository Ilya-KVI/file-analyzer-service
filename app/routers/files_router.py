from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates

from app.database import SessionLocal
from app.models.file import DownloadedFile
from app.services.statistics_service import StatisticsService


router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/files")
def files(request: Request):

    db = SessionLocal()

    try:

        files = (
            db.query(DownloadedFile)
            .order_by(
                DownloadedFile.downloaded_at.desc()
            )
            .all()
        )

        return templates.TemplateResponse(
            request=request,
            name="files.html",
            context={
                "request": request,
                "files": files
            }
        )

    finally:
        db.close()



@router.post("/calculate")
def calculate(
        request: Request,
        files: list[str] = Form(...)
):

    service = StatisticsService()

    result = service.calculate(files)

    return templates.TemplateResponse(
        request=request,
        name="statistics.html",
        context={
            "request": request,
            "statistics": result
        }
    )