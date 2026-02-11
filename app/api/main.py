# app/api/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.inference.model import DummyModel

app = FastAPI(title="ML Inference API", version="1.0")

model = DummyModel()  # load model at startup

# Health check
@app.get("/health")
def health():
    return {"status": "healthy"}

# Predict endpoint
class InputData(BaseModel):
    text: str = "txt"

@app.post("/predict")
def predict(data: InputData):
    try:
        prediction = model.predict(data.text)
        return {"input": data.text, "prediction": prediction}
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))

"""
@app.post("/predict")
def predict(data: InputData):
    return {"input": data.text, "prediction": "dummy_result"}

# Square numbers endpoint
class NumberData(BaseModel):
    numbers: list[int] = [1, 2, 3]

@app.post("/square_numbers")
def square_number(data: NumberData):
    try:
        squared = [x**2 for x in data.numbers]
        return {"original": data.numbers, "squared": squared}
    except Exception as e:
        return {"error": str(e)}
# other parts will be added while using cloud including security and etc

"""