class ProgressService:

    progress = {
        "status": "Ожидание",
        "downloaded": 0,
        "total": 0,
        "percent": 0,
        "current_batch": 0,
        "message": ""
    }

    @classmethod
    def update(
            cls,
            status,
            downloaded,
            current_batch,
            message,
            total=0
    ):

        percent = 0

        if total:
            percent = int(downloaded / total * 100)

        cls.progress = {
            "status": status,
            "downloaded": downloaded,
            "total": total,
            "percent": percent,
            "current_batch": current_batch,
            "message": message
        }

    @classmethod
    def get(cls):

        return cls.progress