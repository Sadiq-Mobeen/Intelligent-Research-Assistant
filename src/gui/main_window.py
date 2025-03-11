import tkinter as tk
from tkinter import ttk
import sys
import os

sys.path.append("src/gui/components")
print("Python Path in main_window:", sys.path)

from model_selector import ModelSelector
from chat_box import ChatBox
from output_panel import OutputPanel
from pdf_browser import PDFBrowser
from history_section import HistorySection
from save_button import SaveButton


class MainWindow(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding="10 10 10 10")
        self.parent = parent
        parent.resizable(False, False)
        self.model_selector = ModelSelector(self)
        self.chat_box = None
        self.reasoning_output = None
        self.result_output = None
        self.pdf_browser_button = None
        self.history_section = None
        self.save_button = None

        self.setup_ui()

    def setup_ui(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Model Selector
        model_selector_label = ttk.Label(self, text="Select Model:")
        model_selector_label.grid(column=0, row=0, sticky=tk.W)
        self.model_selector.grid(column=1, row=0, sticky=(tk.W + tk.E))

        # Chat Box
        chat_box_label = ttk.Label(self, text="Chat Box:")
        # Output Panel (Reasoning and Result)
        output_panel_label = ttk.Label(self, text="Output:")
        output_panel_label.grid(column=0, row=2, sticky=tk.W)
        self.output_panel = OutputPanel(self)
        self.output_panel.grid(column=1, row=2, sticky=(tk.W + tk.E))

        # Chat Box
        chat_box_label = ttk.Label(self, text="Chat Box:")
        chat_box_label.grid(column=0, row=1, sticky=tk.W)
        # from chat_box import ChatBox
        self.chat_box = ChatBox(self, ollama_handler=self.model_selector.ollama, output_panel=self.output_panel)
        self.chat_box.grid(column=1, row=1, sticky=(tk.W + tk.E))

        # PDF Browser
        pdf_browser_label = ttk.Label(self, text="PDF File:")
        pdf_browser_label.grid(column=0, row=3, sticky=tk.W)
        self.pdf_browser = PDFBrowser(self)
        self.pdf_browser.grid(column=1, row=3, sticky=(tk.W + tk.E))

        # History Section
        history_label = ttk.Label(self, text="History:")
        history_label.grid(column=0, row=4, sticky=tk.W)
        self.history_section = HistorySection(self)
        self.history_section.grid(column=1, row=4, sticky=(tk.W + tk.E))

        # Save Button
        save_button_label = ttk.Label(self, text="Save Output:")
        save_button_label.grid(column=0, row=5, sticky=tk.W)
        self.save_button = SaveButton(self)
        self.save_button.grid(column=1, row=5, sticky=(tk.W + tk.E))

        self.pack(fill=tk.BOTH, expand=True)
