import requests
import os
import sys
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

sys.path.append(os.path.abspath('src/config'))
sys.path.append(os.path.abspath('src/utils'))

print("Python Path after appending 'config' and 'utils':", sys.path)

from settings import settings
import logging

logger = logging.getLogger(__name__)

class OllamaHandler:
    def __init__(self):
        self.base_url = settings.OLLAMA_HOST
        self.conversation_history = []
        self.pdf_chunks = [] # store pdf content chunks
        self.session = requests.Session()
        retry_strategy = Retry(
            total=3,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET", "POST"]
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

    def list_models(self):
        """Get available Ollama models"""
        try:
            response = self.session.get(f"{self.base_url}/api/tags")
            if response.status_code == 200:
                return [model["name"] for model in response.json()["models"]]
            else:
                logger.error(f"Failed to get models. Status code: {response.status_code}")
                return []
        except Exception as e:
            logger.error(f"Model listing failed: %s", str(e))
            return []

    def generate_response(self, model: str, prompt: str):
        """Send prompt to Ollama model and maintain history"""
        self.conversation_history.append({"role": "user", "content": prompt})
        context = [item["content"] for item in self.conversation_history]
        if self.pdf_chunks:
            pdf_context_message = "You have been provided with the content of a PDF document in the following context. Please use this information to answer the user's question.\n\nPDF Content:\n"
            context = [pdf_context_message] + self.pdf_chunks + context

        if self.pdf_chunks:
            pdf_context_message = "You have been provided with the content of a PDF document. Please use this information to answer the user's question.\n\nPDF Content:\n"
            pdf_content = "".join(self.pdf_chunks) # Concatenate chunks into single string
        if self.pdf_chunks:
            pdf_context_message = "You have provided a PDF document. Here is the content of the PDF:\n\n"
            pdf_content = "".join(self.pdf_chunks)
            prompt_with_context = pdf_context_message + pdf_content + "\n\nUser Instruction: " + prompt
        else:
            prompt_with_context = prompt

        payload = {
            "model": model,
            "prompt": prompt_with_context,
            "stream": False,
        }

        try:
            url = f"{self.base_url}/api/generate"
            logger.debug(f"Request URL: {url}") # Log the request URL
            logger.debug(f"Request payload: {payload}") # Log the payload
            response = self.session.post(
                url,
                json=payload,
                timeout=120
            )
            logger.debug(f"Response status code: {response.status_code}") # Log status code
            logger.debug(f"Response headers: {response.headers}") # Log headers
            if response.status_code == 200:
                full_response = response.json()["response"]
                reasoning = ""
                if "<think>" in full_response and "</think>" in full_response:
                    reasoning_start = full_response.find("<think>") + len("<think>")
                    reasoning_end = full_response.find("</think>")
                    reasoning = full_response[reasoning_start:reasoning_end].strip()
                    model_response = full_response.replace("<think>", "").replace("</think>", "").strip()
                else:
                    model_response = full_response
                self.conversation_history.append({"role": "assistant", "content": model_response})
                return {"response": model_response, "reasoning": reasoning}
            else:
                logger.error(f"Failed to generate response. Status code: {response.status_code}")
                logger.error(f"Response content: {response.content}") # Log response content
                return "Error: Failed to generate response"
        except requests.exceptions.RequestException as e: # Catch network errors
            logger.error(f"Request exception: %s", str(e))
            return "Error: Model unavailable"
        except Exception as e:
            logger.error(f"Generation failed: %s", str(e))
            return "Error: Model unavailable"

    def start_session(self):
        """Start a new session and clear history"""
        self.conversation_history = []
        self.clear_pdf() # clear pdf too

    def load_pdf(self, chunks):
        self.pdf_chunks = chunks

    def end_session(self):
        """Clears the current session data (history and pdf)"""
        self.conversation_history = []
        self.pdf_chunks = []

    def clear_pdf(self): # Reverted to alias for end_session for clarity in UI logic
        """Alias for end_session for clarity in UI logic"""
        self.end_session()

