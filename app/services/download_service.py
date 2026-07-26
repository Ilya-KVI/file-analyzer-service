import io
import time
import zipfile
from datetime import datetime


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

            file_names = self.client.get_file_names()


            if not file_names:
                print("Все файлы скачаны!")
                break


            print(
                f"Получены файлы: {file_names}"
            )


            for i in range(0, len(file_names), 3):

                batch = file_names[i:i+3]


                zip_data = self.client.download_files(batch)


                self.extract_zip(zip_data)


                self.storage_service.save_files(
                    self.db,
                    batch
                )


                self.client.mark_downloaded(batch)


                time.sleep(2)


                total_downloaded += len(batch)


                print(
                    f"Скачано всего: {total_downloaded}"
                )



        return {
            "downloaded": total_downloaded,
            "finished_at": datetime.now()
        }



    def extract_zip(self, data):

        with zipfile.ZipFile(io.BytesIO(data)) as archive:

            for filename in archive.namelist():

                archive.extract(
                    filename,
                    "app/downloads"
                )

                print(f"Файл распакован: {filename}")