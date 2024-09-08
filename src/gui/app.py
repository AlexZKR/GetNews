import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self, title, size, isResizeble):
        super().__init__()
        
        #main setup
        self.title(title)
        self.geometry(f"{size[1]}x{size[0]}")
        self.minsize(size[1], size[0])
        self.resizable(width=isResizeble, height=isResizeble)
        self.mainloop()
        
        #widgets


App("Web scraper 3.0", (500, 400), False)
