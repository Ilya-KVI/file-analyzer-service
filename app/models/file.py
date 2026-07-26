from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.database import Base


class DownloadedFile(Base):

    __tablename__ = "downloaded_files"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    filename = Column(
        String,
        unique=True,
        nullable=False
    )


    downloaded_at = Column(
        DateTime,
        default=datetime.utcnow
    )