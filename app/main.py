from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.model import MLModel

app = FastAPI()
ml_model = MLModel("model/model.pkl")

class PredictRequest(BaseModel):
    features: list[float]

class PredictResponse(BaseModel):
    prediction: float

@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    try:
        prediction = ml_model.predict(request.features)
        return PredictResponse(prediction=prediction)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Internal model error")