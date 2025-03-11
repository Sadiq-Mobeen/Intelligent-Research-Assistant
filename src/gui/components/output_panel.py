import tkinter as tk
from tkinter import ttk

class OutputPanel(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.notebook = ttk.Notebook(self)

        self.reasoning_tab = ttk.Frame(self.notebook)
        self.result_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.reasoning_tab, text="Reasoning")
        self.notebook.add(self.result_tab, text="Result")

        self.reasoning_text = tk.Text(self.reasoning_tab, height=10, width=50)
        self.result_text = tk.Text(self.result_tab, height=10, width=50)

        self.reasoning_text.pack(fill=tk.BOTH, expand=True)
        self.result_text.pack(fill=tk.BOTH, expand=True)
        self.notebook.pack(fill=tk.BOTH, expand=True)

    def set_reasoning_text(self, text):
        self.reasoning_text.delete("1.0", tk.END)
        self.reasoning_text.insert(tk.END, text)

    def set_result_text(self, text):
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, text)