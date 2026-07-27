from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base
from app.models.file import DownloadedFile
from app.services.file_storage_service import FileStorageService


def test_save_files():

    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={
            "check_same_thread": False
        }
    )


    TestingSessionLocal = sessionmaker(
        bind=engine
    )


    Base.metadata.create_all(
        bind=engine
    )


    db = TestingSessionLocal()


    service = FileStorageService()


    service.save_files(
        db,
        [
            "test1.txt",
            "test2.txt"
        ]
    )


    files = db.query(
        DownloadedFile
    ).all()


    assert len(files) == 2

    assert files[0].filename == "test1.txt"

    assert files[1].filename == "test2.txt"


    db.close()