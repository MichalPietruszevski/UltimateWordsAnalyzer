import tkinter as tk

class Word_cloud_app:
    #Set initial operactions
    def __init__(self, master):
        self.master = master
        self.master.title("Ultimate Words Analyzer 01.00 - Word's Cloud Generator")
        self.master.geometry("400x200")
        self.master.iconbitmap('static/open-book.ico')

        self.frame = tk.Frame(self.master)
        self.frame.pack()
