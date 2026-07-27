import io
import zipfile

from app.services.download_service import DownloadService


class FakeClient:


    def __init__(self):

        self.calls = 0
        self.marked_files = []


    def get_file_names(self):

        self.calls += 1


        if self.calls == 1:
            return [
                "file1.txt",
                "file2.txt"
            ]


        return []


    def download_files(self, file_names):

        memory_file = io.BytesIO()


        with zipfile.ZipFile(
                memory_file,
                "w"
        ) as archive:

            for file_name in file_names:

                archive.writestr(
                    file_name,
                    "1122334455"
                )


        return memory_file.getvalue()



    def mark_downloaded(self, file_names):

        self.marked_files.extend(
            file_names
        )



class FakeStorage:


    def __init__(self):

        self.saved_files = []



    def save_files(
            self,
            db,
            file_names
    ):

        self.saved_files.extend(
            file_names
        )



def test_download_all_files(tmp_path):


    client = FakeClient()


    storage = FakeStorage()



    service = DownloadService(
        client,
        storage,
        None
    )


    service.extract_zip = lambda data: None



    result = service.download_all_files()



    assert result["downloaded"] == 2


    assert storage.saved_files == [
        "file1.txt",
        "file2.txt"
    ]


    assert client.marked_files == [
        "file1.txt",
        "file2.txt"
    ]