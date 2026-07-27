from unittest.mock import Mock, patch

from app.services.file_client import FileClient


def test_get_file_names():

    client = FileClient(
        "http://test.com",
        "Ilya-KVI"
    )


    mock_response = Mock()

    mock_response.json.return_value = {
        "file_names": [
            "file1.txt",
            "file2.txt"
        ]
    }


    with patch(
            "app.services.file_client.requests.request",
            return_value=mock_response
    ) as request_mock:


        result = client.get_file_names()


    assert result == [
        "file1.txt",
        "file2.txt"
    ]


    request_mock.assert_called_once()



def test_download_files():

    client = FileClient(
        "http://test.com",
        "Ilya-KVI"
    )


    mock_response = Mock()

    mock_response.content = b"zip data"


    with patch(
            "app.services.file_client.requests.request",
            return_value=mock_response
    ):


        result = client.download_files(
            [
                "1.txt",
                "2.txt"
            ]
        )


    assert result == b"zip data"



def test_mark_downloaded():

    client = FileClient(
        "http://test.com",
        "Ilya-KVI"
    )


    mock_response = Mock()

    mock_response.json.return_value = {
        "marked_now": 2,
        "already_marked": 0
    }


    with patch(
            "app.services.file_client.requests.request",
            return_value=mock_response
    ):


        result = client.mark_downloaded(
            [
                "1.txt",
                "2.txt"
            ]
        )


    assert result["marked_now"] == 2