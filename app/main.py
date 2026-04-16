from fastapi import FastAPI, WebSocket
from .routes import router
from .websocket import websocket_endpoint

app = FastAPI()

# REST routes
app.include_router(router)

# WebSocket route
@app.websocket("/ws/stream")
async def websocket_route(websocket: WebSocket):
    await websocket_endpoint(websocket)


@app.get("/")
def home():
    return {"message": "API running"}