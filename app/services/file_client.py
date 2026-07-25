import requests


class FileClient:

    def __init__(self, base_url: str, candidate_id: str):
        self.base_url = base_url
        self.headers = {
            "X-Candidate-Id": candidate_id
        }


    def get_file_names(self):
        response = requests.get(
            f"{self.base_url}/api/files/names",
            headers=self.headers
        )

        response.raise_for_status()

        return response.json()["file_names"]


    def download_files(self, file_names: list[str]):
        response = requests.post(
            f"{self.base_url}/api/files/download",
            headers=self.headers,
            json={
                "file_names": file_names
            }
        )

        response.raise_for_status()

        return response.content


    def mark_downloaded(self, file_names: list[str]):
        response = requests.post(
            f"{self.base_url}/api/files/downloaded",
            headers=self.headers,
            json={
                "file_names": file_names
            }
        )

        response.raise_for_status()

        return response.json()