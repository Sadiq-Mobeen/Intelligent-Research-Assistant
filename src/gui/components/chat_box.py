import tkinter as tk
from tkinter import ttk

class ChatBox(ttk.Frame):
    def __init__(self, main_window, ollama_handler, output_panel):
        super().__init__(main_window) # Pass main_window as parent
        self.main_window = main_window # Store main_window instance
        self.ollama_handler = ollama_handler
        self.output_panel = output_panel
        self.text_area = tk.Text(self, height=10, width=50)
        self.send_button = ttk.Button(self, text="Send", command=self.send_message)

        self.send_button.pack(side=tk.LEFT, fill=tk.X)
        self.text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.session_frame = ttk.Frame(self)  # Frame for session buttons
        self.start_session_button = ttk.Button(self.session_frame, text="Start Session", command=self.start_session)
        self.end_session_button = ttk.Button(self.session_frame, text="End Session", command=self.end_session, state=tk.DISABLED) # Initially disabled
        self.session_frame.pack(fill=tk.X) # Pack session frame below buttons
        self.start_session_button.pack(side=tk.LEFT)
        self.end_session_button.pack(side=tk.LEFT)

        self.is_session_active = False # Track session state

    def start_session(self):
        print("Start Session clicked") # Placeholder
        self.is_session_active = True
        self.start_session_button.config(state=tk.DISABLED)
        self.end_session_button.config(state=tk.NORMAL)
        self.ollama_handler.end_session() # Call ollama_handler.end_session

    def end_session(self):
        print("End Session clicked") # Placeholder
        self.is_session_active = False
        self.start_session_button.config(state=tk.NORMAL)
        self.end_session_button.config(state=tk.DISABLED)
        self.ollama_handler.end_session() # Call ollama_handler.end_session - corrected method name

    def send_message(self):
        message = self.text_area.get("1.0", tk.END).strip()
        if message and self.is_session_active: # Check if session is active
            # Placeholder for message sending logic
            model = self.main_window.model_selector.model_var.get() # Get selected model from ModelSelector using main_window
            response_dict = self.ollama_handler.generate_response(model, message)
            if response_dict and "response" in response_dict and not response_dict["response"].startswith("Error"): # Check for errors explicitly
                message_content = response_dict["response"]
                reasoning_content = response_dict.get("reasoning", "Not a reasoning model") # Set reasoning text, handle missing reasoning
                self.output_panel.set_reasoning_text(reasoning_content) # Set reasoning text, handle missing reasoning
                self.output_panel.set_result_text(message_content) # Set result text
            else:
                self.output_panel.set_reasoning_text("Error")
                self.output_panel.set_result_text("Failed to get response from model. Please check console for errors.") # User-friendly error message