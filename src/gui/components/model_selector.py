import tkinter as tk
from tkinter import ttk

import os
import sys

print("Current working directory in model_selector:", os.getcwd())
print("Absolute path of 'src' directory:", os.path.abspath('src'))
print("Python Path in model_selector:", sys.path)

sys.path.append(os.path.abspath('src/handlers'))
print("Python Path after appending 'src/handlers':", sys.path)

from ollama_handler import OllamaHandler

class ModelSelector(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.ollama = OllamaHandler()
        
        self.model_var = tk.StringVar()
        self.combobox = ttk.Combobox(self, textvariable=self.model_var)
        self.refresh_btn = ttk.Button(self, text="🔄", command=self.refresh_models)
        
        self.combobox.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.refresh_btn.pack(side=tk.RIGHT)
        self.refresh_models()

    def refresh_models(self):
        models = self.ollama.list_models()
        self.combobox["values"] = models
        if models:
            self.model_var.set(models[0])