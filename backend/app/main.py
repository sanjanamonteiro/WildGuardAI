from fastapi import FastAPI

app = FastAPI(title="WildGuard AI")

@app.get("/")
def home():
    return {
        "message": "WildGuard AI backend is running"
    }