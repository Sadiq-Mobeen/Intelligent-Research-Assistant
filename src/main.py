import sys
import os
sys.path.insert(0, os.path.abspath('src')) # Add src directory to Python path
print("Python Path:", sys.path)

import tkinter as tk
from gui.main_window import MainWindow
from utils.logger import setup_logging

def main():
    setup_logging()
    root = tk.Tk()
    root.title("Intelligent PDF Assistant")
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()