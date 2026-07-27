from app.services.statistics_service import StatisticsService


def test_calculate_statistics(tmp_path):

    file = tmp_path / "test.txt"

    file.write_text(
        "1122334455",
        encoding="utf-8"
    )


    service = StatisticsService(
        download_dir=str(tmp_path)
    )


    result = service.calculate(
        ["test.txt"]
    )


    assert result["total"]["1"] == 2
    assert result["total"]["2"] == 2
    assert result["total"]["3"] == 2