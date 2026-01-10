from fastapi import FastAPI
import uvicorn

app = FastAPI()

users = [
    {"id": 1, "name": "Raj"},
    {"id": 2, "name": "Amit"},
    {"id": 3, "name": "Neha"}
]

@app.get("/users")
def get_users():
    return users

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
