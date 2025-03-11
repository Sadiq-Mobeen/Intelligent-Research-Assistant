import tkinter as tk
from tkinter import ttk, filedialog
import sys

sys.path.append("src/handlers")

from pdf_handler import PDFHandler




class PDFBrowser(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pdf_path_var = tk.StringVar()
        self.browse_button = ttk.Button(self, text="Browse PDF", command=self.browse_pdf)
        self.pdf_path_label = ttk.Label(self, textvariable=self.pdf_path_var)
        self.main_window = parent # Store main_window instance

        self.browse_button.pack(side=tk.LEFT)
        self.pdf_path_label.pack(side=tk.LEFT, fill=tk.X, expand=True)

    def browse_pdf(self):
        file_path = filedialog.askopenfilename(
            title="Select a PDF file",
            filetypes=[("PDF files", "*.pdf")]
        )
        if file_path:
            self.pdf_path_var.set(file_path)
            self.load_pdf_content(file_path) # Call load_pdf_content

    def load_pdf_content(self, file_path):
        pdf_handler = PDFHandler()
        text_content = pdf_handler.extract_text(file_path)
        chunks = pdf_handler.chunk_text(text_content)
        self.main_window.chat_box.ollama_handler.load_pdf(chunks) # Access ollama_handler via main_window
        print(f"PDF loaded and text extracted in chunks.") # Confirmation message