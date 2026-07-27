from collections import Counter
from pathlib import Path


class StatisticsService:

    def calculate(self, file_names: list[str]):

        total_counter = Counter()

        files_statistics = {}

        for file_name in file_names:

            path = Path("app/downloads") / file_name

            with open(path, "r", encoding="utf-8") as file:
                content = file.read().strip()

            counter = Counter(content)

            files_statistics[file_name] = dict(counter)

            total_counter.update(counter)

        return {
            "total": dict(total_counter),
            "files": files_statistics
        }