from fastapi import WebSocket, WebSocketDisconnect
from .services.inference import predict_anomaly
import json

async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("Client connected")

    try:
        while True:
            # Receive data
            data = await websocket.receive_text()
            data = json.loads(data)

            # Predict
            result = predict_anomaly(data)

            # Send response
            await websocket.send_json({
                "anomaly": result
            })

    except WebSocketDisconnect:
        print("Client disconnected")