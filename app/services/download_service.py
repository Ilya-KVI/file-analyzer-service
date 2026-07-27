import io
import time
import zipfile
from datetime import datetime
from pathlib import Path
from app.services.progress_service import ProgressService

MAX_FILES_PER_REQUEST = 3
REQUEST_DELAY = 2
DOWNLOAD_DIR = Path("app/downloads")


class DownloadService:


    def __init__(
            self,
            client,
            storage_service,
            db
    ):
        self.client = client
        self.storage_service = storage_service
        self.db = db



    def download_all_files(self):

        total_downloaded = 0


        while True:

            ProgressService.update(
                "Скачивание началось",
                total_downloaded,
                0,
                "Получение списка файлов"
            )

            file_names = self.client.get_file_names()


            if not file_names:

                ProgressService.update(
                    "Завершено",
                    total_downloaded,
                    0,
                    "Все файлы скачаны!"
                )

                print("Все файлы скачаны!")
                break


            print(
                f"Получены файлы: {file_names}"
            )

            ProgressService.update(
                "Скачивание",
                total_downloaded,
                len(file_names),
                f"Получено {len(file_names)} названий файлов"
            )


            for i in range(
                   0,
                   len(file_names),
                   MAX_FILES_PER_REQUEST
            ):


                batch = file_names[
                   i:i + MAX_FILES_PER_REQUEST
               ]


                zip_data = self.client.download_files(batch)


                self.extract_zip(zip_data)


                self.storage_service.save_files(
                    self.db,
                    batch
                )


                self.client.mark_downloaded(batch)


                time.sleep(REQUEST_DELAY)


                total_downloaded += len(batch)


                ProgressService.update(
                    "Скачивание",
                    total_downloaded,
                    len(batch),
                    f"Скачано {total_downloaded} файлов"
                )


                print(
                    f"Скачано всего: {total_downloaded}"
                )



        return {
            "downloaded": total_downloaded,
            "finished_at": datetime.now()
        }



    def extract_zip(self, data):

        DOWNLOAD_DIR.mkdir(
            exist_ok=True
        )

        try:

            with zipfile.ZipFile(io.BytesIO(data)) as archive:

                for filename in archive.namelist():

                    archive.extract(
                        filename,
                        DOWNLOAD_DIR
                    )

                    print(
                        f"Файл распакован: {filename}"
                    )

        except zipfile.BadZipFile:

            print(
                "Ошибка: получен некорректный ZIP архив"
            )

            raise