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

```text
realtime-anomaly-detection/
│
├── app/
│   ├── main.py
│   ├── routes.py
│   ├── websocket.py
│   ├── schemas.py
│   │
│   ├── services/
│   │   ├── inference.py
│   │   ├── cache.py
│   │
│   ├── ml/
│   │   ├── train.py
│   │   ├── model.pkl
│
├── scripts/
│   ├── simulate_stream.py
│   ├── test.py
│
├── requirements.txt
└── README.md

```

## 📊 Dataset

This project uses the **Credit Card Fraud Detection dataset**:

👉 https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

### Setup

1. Download the dataset from Kaggle  
2. Place the file as: app/ml/creditcard.csv

⚠️ Note: Dataset is not included in this repository due to size limitations.

---

## ⚡ How It Works

1. Client sends streaming data via WebSocket  
2. Backend processes data asynchronously  
3. Data is passed to ML model  
4. Cache is checked  
5. Result is returned instantly  
---
## 🧪 Running the Project


### 1. Clone the repository

```bash
git clone https://github.com/nishithaNsingh/realtime-anomaly-detection
cd realtime-anomaly-detection
````

---

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Train the model

```bash
cd app/ml
python train.py
```

---

### 5. Run the server

```bash
uvicorn app.main:app --reload
```

---

### 6. Test API

Open in browser:

```
http://127.0.0.1:8000/docs
```


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

