import asyncio
import websockets
import json
import random

async def send_data():
    uri = "ws://127.0.0.1:8000/ws/stream"

    async with websockets.connect(uri) as websocket:
        while True:
            # 90% anomalies
            if random.random() < 0.9:
                data = {
                    "V1": random.uniform(-10, 10),
                    "V2": random.uniform(-10, 10),
                    "V3": random.uniform(-10, 10),
                    "V4": random.uniform(-10, 10),
                    "V5": random.uniform(-10, 10),
                    "V6": random.uniform(-10, 10),
                    "V7": random.uniform(-10, 10),
                    "V8": random.uniform(-10, 10),
                    "V9": random.uniform(-10, 10),
                    "V10": random.uniform(-10, 10),
                    "V11": random.uniform(-10, 10),
                    "V12": random.uniform(-10, 10),
                    "V13": random.uniform(-10, 10),
                    "V14": random.uniform(-10, 10),
                    "V15": random.uniform(-10, 10),
                    "V16": random.uniform(-10, 10),
                    "V17": random.uniform(-10, 10),
                    "V18": random.uniform(-10, 10),
                    "V19": random.uniform(-10, 10),
                    "V20": random.uniform(-10, 10),
                    "V21": random.uniform(-10, 10),
                    "V22": random.uniform(-10, 10),
                    "V23": random.uniform(-10, 10),
                    "V24": random.uniform(-10, 10),
                    "V25": random.uniform(-10, 10),
                    "V26": random.uniform(-10, 10),
                    "V27": random.uniform(-10, 10),
                    "V28": random.uniform(-10, 10),
                    "Amount": random.uniform(50000, 100000)  # extreme
                }
                label = "ANOMALY"

            # 10% normal
            else:
                data = {
                    "V1": random.uniform(-2, 2),
                    "V2": random.uniform(-2, 2),
                    "V3": random.uniform(-2, 2),
                    "V4": random.uniform(-2, 2),
                    "V5": random.uniform(-2, 2),
                    "V6": random.uniform(-2, 2),
                    "V7": random.uniform(-2, 2),
                    "V8": random.uniform(-2, 2),
                    "V9": random.uniform(-2, 2),
                    "V10": random.uniform(-2, 2),
                    "V11": random.uniform(-2, 2),
                    "V12": random.uniform(-2, 2),
                    "V13": random.uniform(-2, 2),
                    "V14": random.uniform(-2, 2),
                    "V15": random.uniform(-2, 2),
                    "V16": random.uniform(-2, 2),
                    "V17": random.uniform(-2, 2),
                    "V18": random.uniform(-2, 2),
                    "V19": random.uniform(-2, 2),
                    "V20": random.uniform(-2, 2),
                    "V21": random.uniform(-2, 2),
                    "V22": random.uniform(-2, 2),
                    "V23": random.uniform(-2, 2),
                    "V24": random.uniform(-2, 2),
                    "V25": random.uniform(-2, 2),
                    "V26": random.uniform(-2, 2),
                    "V27": random.uniform(-2, 2),
                    "V28": random.uniform(-2, 2),
                    "Amount": random.uniform(10, 1000)
                }
                label = "NORMAL"

            # Send data
            await websocket.send(json.dumps(data))

            # Receive response
            response = await websocket.recv()

            print(f"Input: {label} | Server response: {response}")

            await asyncio.sleep(1)

asyncio.run(send_data())