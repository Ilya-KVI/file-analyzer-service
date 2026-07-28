from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from app.routers.calculate_router import router as calculate_router

from app.database import engine
from app.database import Base

import os

from dotenv import load_dotenv

from app.routers.download_router import router as download_router

from app.routers.files_router import router as files_router

from app.routers.progress_router import router as progress_router

load_dotenv()

app = FastAPI(
    title="File Analyzer Service"
)

Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

app.include_router(download_router)

app.include_router(files_router)

app.include_router(calculate_router)

app.include_router(progress_router)


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