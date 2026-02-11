from app.core.logger import logger
from app.core.config import DEFAULT_TEXT

class DummyModel:
    def __init__(self, default_text=DEFAULT_TEXT):
        self.default_text = default_text

    def predict(self, text: str) -> str:
        if not text:
            text = self.default_text
        try:
            result = f"predicted({text})"
            logger.info("Model prediction successful for input: %s", text)
            return result
        except Exception as e:
            logger.error("Inference error: %s", str(e))
            raise RuntimeError(f"Inference error: {str(e)}")
