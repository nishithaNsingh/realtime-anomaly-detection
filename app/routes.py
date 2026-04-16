from fastapi import APIRouter
from .schemas import Transaction
from .services.inference import predict_anomaly

router = APIRouter()

@router.post("/predict")
async def predict(transaction: Transaction):
    result = predict_anomaly(transaction.dict())
    return {"anomaly": result}
