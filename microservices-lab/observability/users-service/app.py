from fastapi import FastAPI
import uvicorn

from prometheus_client import Counter, generate_latest
from fastapi import Response

REQUEST_COUNT = Counter("requests_total", "Total Requests")

app = FastAPI()

users = [
    {"id": 1, "name": "Raj"},
    {"id": 2, "name": "Amit"},
    {"id": 3, "name": "Neha"}
]

@app.get("/users")
def get_users():
    return users

@app.middleware("http")
async def count_requests(request, call_next):
    REQUEST_COUNT.inc()
    return await call_next(request)

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
