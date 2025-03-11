import pickle
from pathlib import Path
from config.settings import settings

class CacheManager:
    def __init__(self):
        self.cache_dir = Path(settings.CACHE_DIR)
        self.cache_dir.mkdir(exist_ok=True)
        
    def get_pdf(self, file_path: str) -> str | None:
        # ... (implementation)
        pass
        
    def save_pdf(self, file_path: str, text: str):
        # ... (implementation)
        pass