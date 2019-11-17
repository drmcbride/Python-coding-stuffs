# imports

import tkinter as tk
from tkinter import filedialog, Text
import os
# gui
root = tk.Tk()
root.title("Uno game")
canvas = tk.Canvas(root, height=700, width=700, bg="#FF0000")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.9, relheight=0.9, relx=.05, rely=0.05)
Uno = tk.Button(root, text="Start Uno?", padx=300,
                pady=3, fg="blue", bg="#00FF7F")
Uno.pack()


root.mainloop()
# Def

