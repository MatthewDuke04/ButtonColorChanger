import tkinter as tk
from tkinter import Label, PhotoImage, filedialog, Text
import os
import random




root = tk.Tk()
root.geometry=("700x700")
root.title("Button Changes Background Color")

canvasColor = "White"

def colorchange():
    colors = ["purple", "blue", "red", "green", "yellow", "black", "white", "pink", "orange", "indigo"]
    canvas.config(bg=random.choice(colors))
    canvas.pack()
        

canvas = tk.Canvas(root, height=700, width=700, bg=canvasColor)
canvas.pack()


changecolor = tk.Button(root, text="Change Color", padx=20, pady=15, bg= "black", fg= "white", command= colorchange)
changecolor.pack(expand=True)


value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


root.mainloop()
