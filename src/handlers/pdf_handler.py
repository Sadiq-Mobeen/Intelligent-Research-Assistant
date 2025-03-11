import pdfplumber
from pathlib import Path
import sys

sys.path.append("src/utils")

from cache_maneger import CacheManager

class PDFHandler:
    def __init__(self):
        self.cache = CacheManager()
        
    def extract_text(self, file_path: str) -> str:
        """Extract and cache PDF text"""
        if cached := self.cache.get_pdf(file_path):
            return cached
            
        text = ""
        with pdfplumber.open(file_path) as pdf:
            full_text = {}
            for i, page in enumerate(pdf.pages):
                page_text = page.extract_text()
                if page_text.strip():  # Add non-empty pages
                    full_text[f"Page {i+1}"] = page_text
        
        # Convert the dictionary to a single string for caching and return
        text = "\n".join([f"<{section_name}>\n{content}\n</{section_name}>" for section_name, content in full_text.items()])
        self.cache.save_pdf(file_path, text)
        return text

    def chunk_text(self, text: str, chunk_size=2000) -> list[str]:
        """Split text for LLM context window"""
        return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]