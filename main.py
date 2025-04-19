# main.py
from tkinter import Tk
from src.gui import LectureSummarizerApp

if __name__ == "__main__":
    root = Tk()
    app = LectureSummarizerApp(root)
    root.mainloop()
