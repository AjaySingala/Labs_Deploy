from fastapi import FastAPI
import requests
import uvicorn

app = FastAPI()

USERS_SERVICE_URL = "http://users-service:8001/users"

@app.get("/orders")
def get_orders():
    users = requests.get(USERS_SERVICE_URL).json()
    orders = [{"order_id": i+1, "user": u["name"]} for i, u in enumerate(users)]
    return {"orders": orders}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)
