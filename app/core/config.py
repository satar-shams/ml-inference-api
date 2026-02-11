import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

APP_HOST = os.getenv("APP_HOST", "127.0.0.1")
APP_PORT = int(os.getenv("APP_PORT", 8000))
MODEL_PATH = os.getenv("MODEL_PATH", "app/inference/model.py")
DEFAULT_TEXT = os.getenv("DEFAULT_TEXT", "Hello")
