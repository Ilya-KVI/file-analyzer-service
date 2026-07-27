from fastapi import APIRouter

from app.services.progress_service import ProgressService


router = APIRouter()


@router.get("/progress")
def progress():

    return ProgressService.get()