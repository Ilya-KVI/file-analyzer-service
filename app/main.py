from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
    "message": "File analyzer service is running"
    }