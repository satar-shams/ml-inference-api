from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.inference.model import DummyModel
from app.core.logger import logger
from app.core.config import APP_HOST, APP_PORT

app = FastAPI(title="ML Inference API", version="1.0")

# Health check
@app.get("/health")
def health():
    logger.info("Health check requested")
    return {"status": "healthy"}

# Predict endpoint
class InputData(BaseModel):
    text: str = None

model = DummyModel()

@app.post("/predict")
def predict(data: InputData):
    input_text = data.text or model.default_text
    logger.info("Received /predict request with input: %s", input_text)
    try:
        prediction = model.predict(input_text)
        logger.info("Prediction successful for input: %s", input_text)
        return {"input": input_text, "prediction": prediction}
    except RuntimeError as e:
        logger.error("Prediction failed for input %s: %s", input_text, str(e))
        raise HTTPException(status_code=500, detail="Internal prediction error")

# Square numbers endpoint
class NumberData(BaseModel):
    numbers: list[int] = [1, 2, 3]

@app.post("/square_numbers")
def square_number(data: NumberData):
    try:
        squared = [x**2 for x in data.numbers]
        logger.info("Squared numbers successfully: %s", squared)
        return {"original": data.numbers, "squared": squared}
    except Exception as e:
        logger.error("Error squaring numbers: %s", str(e))
        raise HTTPException(status_code=500, detail="Internal error")

# Start Uvicorn using config from .env
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.api.main:app", host=APP_HOST, port=APP_PORT, reload=True)
