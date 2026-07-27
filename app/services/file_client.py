import time
import requests

MAX_RETRIES_DELAY = 10
BAN_DELAY = 360
REQUEST_TIMEOUT = 30

class FileClient:

    def __init__(self, base_url: str, candidate_id: str):
        self.base_url = base_url
        self.headers = {
            "X-Candidate-Id": candidate_id
        }

    def _request(
                        self,
                        method,
                        url,
                        **kwargs
                ):

                    while True:

                        try:

                            response = requests.request(
                                method,
                                url,
                                headers=self.headers,
                                timeout=REQUEST_TIMEOUT,
                                **kwargs
                            )

                        except requests.exceptions.RequestException as e:

                            print(
                                f"Ошибка соединения: {e}"
                            )

                            print(
                                f"Повтор через {MAX_RETRIES_DELAY} секунд..."
                            )

                            time.sleep(
                                MAX_RETRIES_DELAY
                            )

                            continue


                        if response.status_code == 429:

                            wait = int(
                                response.headers.get(
                                    "Retry-After",
                                    MAX_RETRIES_DELAY
                                )
                            )

                            print(
                                f"429. Ждем {wait} секунд..."
                            )

                            time.sleep(wait)

                            continue


                        if response.status_code == 403:

                            wait = int(
                                response.headers.get(
                                    "Retry-After",
                                    BAN_DELAY
                                )
                            )

                            print(
                                f"403 BAN. Ждем {wait} секунд..."
                            )

                            time.sleep(wait)

                            continue


                        response.raise_for_status()

                        return response

    def get_file_names(self):

        response = self._request(
            "GET",
            f"{self.base_url}/api/files/names"
        )

        time.sleep(1)

        return response.json()["file_names"]

    def download_files(self, file_names):

        response = self._request(
            "POST",
            f"{self.base_url}/api/files/download",
            json={
                "file_names": file_names[:3]
            }
        )

        time.sleep(1)

        return response.content

    def mark_downloaded(self, file_names):

        response = self._request(
            "POST",
            f"{self.base_url}/api/files/downloaded",
            json={
                "file_names": file_names
            }
        )

        time.sleep(1)

        return response.json()