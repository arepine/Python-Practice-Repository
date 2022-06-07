import tkinter as tk
from tkinter import *

root = tk.Tk(screenName=None, baseName=None, className='Tk', useTk=1)
root.title("RL Browser")

"""
myCanvas = Canvas(root, width=40, height=60)
myCanvas.pack()
canvas_height = 20
canvas_width = 200
y = int(canvas_height / 2)
myCanvas.create_line(0, y, canvas_width, y)
"""
frm = tk.Frame(root)
frm.grid()  

tk.Label(frm, text="Welcome to Repineland!").grid(column=5, row=0)

tk.Button(frm, text="Quit", command=root.destroy).grid(column=5, row=1)
tk.Menubutton(bg="Black", text="Menu")


root.mainloop()