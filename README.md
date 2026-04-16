# 🚀 Real-Time Anomaly Detection Pipeline

## 📌 Overview

This project is a real-time anomaly detection system that processes streaming data using WebSockets and detects anomalies using a machine learning model.

It simulates use cases like fraud detection, log monitoring, and real-time analytics.

---

## ⚙️ Tech Stack

- FastAPI
- WebSockets
- Isolation Forest (scikit-learn)
- Python asyncio
- NumPy, Pandas
- In-memory caching (dict)

---

## 🧠 Architecture

Client (Simulator)
→ WebSocket (FastAPI)
→ Async Processing
→ ML Model (Isolation Forest)
→ Cache Layer
→ Real-Time Response

---

## 🚀 Features

- Real-time streaming using WebSockets  
- Async processing for concurrency  
- ML-based anomaly detection  
- In-memory caching for performance  
- REST API for testing  
- Scalable system design  

---

## 📂 Project Structure

realtime-anomaly-detection/
│
├── app/
│   ├── main.py
│   ├── routes.py
│   ├── websocket.py
│   ├── schemas.py
│   ├── services/
│   │   ├── inference.py
│   │   ├── cache.py
│   ├── ml/
│       ├── train.py
│       ├── model.pkl
│
├── scripts/
│   ├── simulate_stream.py
│   ├── test.py
│
├── requirements.txt
└── README.md

---

## ⚡ How It Works

1. Client sends streaming data via WebSocket  
2. Backend processes data asynchronously  
3. Data is passed to ML model  
4. Cache is checked  
5. Result is returned instantly  

---

## 🧪 Running the Project

### Clone repo
git clone <your-repo-link>
cd realtime-anomaly-detection

### Create venv
python -m venv venv
venv\Scripts\activate

### Install dependencies
pip install -r requirements.txt

### Train model
cd app/ml
python train.py

### Run server
uvicorn app.main:app --reload

### Test API
http://127.0.0.1:8000/docs

### Run streaming simulator
python scripts/simulate_stream.py

### Run anomaly-heavy test
python scripts/test.py

---

## 🧪 Sample Output

Input: ANOMALY → {"anomaly": 1}  
Input: NORMAL → {"anomaly": 0}

---

## 🧠 ML Model

Isolation Forest (unsupervised)

Detects anomalies by isolating data points — anomalies require fewer splits.

---

## ⚡ Performance

- Async processing for low latency  
- Caching to reduce redundant predictions  

---

## 📈 Scalability

- Stateless backend  
- Can scale horizontally  
- Redis can replace in-memory cache  
- Kafka can be added for streaming  


---

## 🔮 Future Improvements

- Redis for caching  
- Kafka for streaming  
- Dashboard UI  
- Cloud deployment  

---

