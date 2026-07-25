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