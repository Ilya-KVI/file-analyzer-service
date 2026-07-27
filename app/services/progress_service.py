class ProgressService:

    progress = {
        "status": "Ожидание",
        "downloaded": 0,
        "current_batch": 0,
        "message": ""
    }


    @classmethod
    def update(
            cls,
            status,
            downloaded,
            current_batch,
            message
    ):

        cls.progress = {
            "status": status,
            "downloaded": downloaded,
            "current_batch": current_batch,
            "message": message
        }


    @classmethod
    def get(cls):

        return cls.progress