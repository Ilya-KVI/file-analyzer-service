from datetime import datetime, UTC

from sqlalchemy.orm import Session

from app.models.file import DownloadedFile


class FileStorageService:


    def save_files(
            self,
            db: Session,
            file_names: list[str]
    ):

        for file_name in file_names:

            existing = db.query(
                DownloadedFile
            ).filter(
                DownloadedFile.filename == file_name
            ).first()


            if not existing:

                file = DownloadedFile(
                    filename=file_name,
                    downloaded_at=datetime.now(UTC)
                )

                db.add(file)


        db.commit()