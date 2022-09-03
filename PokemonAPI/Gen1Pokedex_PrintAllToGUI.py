from tkinter import *
from tkinter import ttk

root = Tk() #root widget, required to start

#GUI size control
root.geometry("400x400")

frame = ttk.Frame(root, padding = 10)

#specify the layout for organizing content
frame.grid()

#provide some text via a label
ttk.Label(frame, text = "Please Enter the Desired Pokemon Name for Information:").grid(column = 0, row = 0)

#quit the app button
ttk.Button(frame, text = 'Quit', command=root.destroy).grid(column=0, row = 15)

#continuously executing app call
root.mainloop()