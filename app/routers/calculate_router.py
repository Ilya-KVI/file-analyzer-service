from fastapi import APIRouter, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request

from app.services.statistics_service import StatisticsService

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.post("/calculate", response_class=HTMLResponse)
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