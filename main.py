import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Simple Image Editor By Musab Al-Bahry")
        #setting window size
        width=862
        height=448
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
