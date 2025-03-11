import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
    CACHE_DIR = os.getenv("CACHE_DIR", "./.cache")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    
settings = Settings()