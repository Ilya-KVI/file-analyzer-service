# File Analyzer Service

A FastAPI-based service for downloading, storing and analyzing text files from an external API.

The application downloads a file catalog in batches, stores information about downloaded files, provides a simple web interface and calculates digit statistics from file contents.

## Features

* Download files from external API
* Batch downloading (maximum 3 files per request)
* Custom candidate identification using `X-Candidate-Id`
* Automatic handling of API rate limits:

    * `429 Too Many Requests`
    * `403 Forbidden`
    * `Retry-After` header support
* ZIP archive extraction
* Store downloaded file information
* Web interface with:

    * file list
    * pagination
    * file selection
    * statistics calculation
* Digit frequency analysis:

    * global statistics
    * statistics per file
* Unit tests with Pytest

## Tech Stack

* Python 3
* FastAPI
* SQLAlchemy
* SQLite
* Jinja2 Templates
* Requests
* Pytest

## Project Structure

```
file-analyzer-service

├── app
│   ├── models
│   │   └── file.py
│   │
│   ├── routers
│   │   ├── calculate_router.py
│   │   ├── download_router.py
│   │   ├── files_router.py
│   │   └── progress_router.py
│   │
│   ├── services
│   │   ├── __init__.py
│   │   ├── download_service.py
│   │   ├── file_client.py
│   │   ├── file_storage_service.py
│   │   ├── progress_service.py
│   │   └── statistics_service.py
│   │
│   ├── __init__.py
│   ├── database.py
│   ├── dependencies.py
│   └── main.py
│
├── templates
│   ├── files.html
│   ├── home.html
│   ├── index.html
│   └── statistics.html
│
├── tests
│   ├── __init__.py
│   ├── test_download_service.py
│   ├── test_file_client.py
│   ├── test_file_storage_service.py
│   └── test_statistics_service.py
│
├── requirements.txt
└── README.md
```

## Architecture

The application is divided into several layers:

```
External API
      |
      v
FileClient
      |
      v
DownloadService
      |
      v
FileStorageService
      |
      v
StatisticsService
```

### FileClient

Responsible for communication with external API:

* getting file names
* downloading files
* marking files as downloaded
* processing API limitations

### DownloadService

Handles the full download workflow:

1. Request available file names
2. Download files in batches
3. Extract ZIP archives
4. Save metadata
5. Mark files as downloaded
6. Repeat until all files are downloaded

### StatisticsService

Analyzes file contents and calculates:

* total digit frequency
* digit frequency for every file

## Installation

Clone repository:

```bash
git clone <repository-url>
```

Navigate to project directory:

```bash
cd file-analyzer-service
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running Application

Start FastAPI server:

```bash
uvicorn app.main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000
```

## Running Tests

Execute:

```bash
pytest
```

Current test result:

```
6 passed
```

## Database

The project uses SQLite database.

Downloaded files are stored with:

* filename
* download timestamp

## Example Workflow

1. Open the web interface
2. Click "Download Data"
3. Wait until all files are downloaded
4. Select files for analysis
5. Click "Calculate Statistics"
6. View digit frequency results

## Additional Notes

The application was developed as a backend test assignment.

The project focuses on:

* clean architecture
* separation of responsibilities
* error handling
* API integration
* automated testing
