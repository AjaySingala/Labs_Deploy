from fastapi import FastAPI
import requests
import uvicorn

from prometheus_client import Counter, generate_latest
from fastapi import Response

REQUEST_COUNT = Counter("requests_total", "Total Requests")

app = FastAPI()

USERS_SERVICE_URL = "http://users-service:8001/users"

@app.get("/orders")
def get_orders():
    users = requests.get(USERS_SERVICE_URL).json()
    orders = [{"order_id": i+1, "user": u["name"]} for i, u in enumerate(users)]
    return {"orders": orders}

@app.middleware("http")
async def count_requests(request, call_next):
    REQUEST_COUNT.inc()
    return await call_next(request)

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)
