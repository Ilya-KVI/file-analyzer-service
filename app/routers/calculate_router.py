from fastapi import APIRouter, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from app.database import SessionLocal
from app.models.file import DownloadedFile
from app.services.statistics_service import StatisticsService


router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.post("/calculate", response_class=HTMLResponse)
def calculate(
        request: Request,
        files: list[str] = Form([]),
        all_files: str = Form("false")
):

    db = SessionLocal()

    try:

        if all_files == "true":

            files = [
                file.filename
                for file in db.query(
                    DownloadedFile
                ).all()
            ]


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


    finally:

        db.close()