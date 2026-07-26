import time

import requests


class FileClient:

    def __init__(self, base_url: str, candidate_id: str):
        self.base_url = base_url
        self.headers = {
            "X-Candidate-Id": candidate_id
        }

    def get_file_names(self):

        while True:

            try:
                response = requests.get(
                    f"{self.base_url}/api/files/names",
                    headers=self.headers,
                    timeout=30
                )

            except requests.exceptions.RequestException as e:
                print(f"Ошибка соединения: {e}")
                print("Повтор через 10 секунд...")
                time.sleep(10)
                continue

            if response.status_code == 429:
                wait = int(response.headers.get("Retry-After", 10))
                print(f"429. Ждем {wait} секунд...")
                time.sleep(wait)
                continue

            if response.status_code == 403:
                wait = int(response.headers.get("Retry-After", 360))
                print(f"403 BAN. Ждем {wait} секунд...")
                time.sleep(wait)
                continue

            response.raise_for_status()

            time.sleep(1)

            return response.json()["file_names"]

    def download_files(self, file_names):

        while True:

            try:
                response = requests.post(
                    f"{self.base_url}/api/files/download",
                    headers=self.headers,
                    json={
                        "file_names": file_names[:3]
                    },
                    timeout=30
                )

            except requests.exceptions.RequestException as e:
                print(f"Ошибка соединения: {e}")
                print("Повтор через 10 секунд...")
                time.sleep(10)
                continue

            if response.status_code == 429:
                wait = int(response.headers.get("Retry-After", 10))
                print(f"429. Ждем {wait} секунд...")
                time.sleep(wait)
                continue

            if response.status_code == 403:
                wait = int(response.headers.get("Retry-After", 360))
                print(f"403 download. Ждем {wait} секунд...")
                time.sleep(wait)
                continue

            response.raise_for_status()

            time.sleep(1)

            return response.content

    def mark_downloaded(self, file_names):

        while True:

            try:
                response = requests.post(
                    f"{self.base_url}/api/files/downloaded",
                    headers=self.headers,
                    json={
                        "file_names": file_names
                    },
                    timeout=30
                )

            except requests.exceptions.RequestException as e:
                print(f"Ошибка соединения: {e}")
                print("Повтор через 10 секунд...")
                time.sleep(10)
                continue

            if response.status_code == 429:
                wait = int(response.headers.get("Retry-After", 10))
                print(f"429 mark. Ждем {wait} секунд...")
                time.sleep(wait)
                continue

            if response.status_code == 403:
                wait = int(response.headers.get("Retry-After", 360))
                print(f"403 mark. Ждем {wait} секунд...")
                time.sleep(wait)
                continue

            response.raise_for_status()

            time.sleep(1)

            return response.json()