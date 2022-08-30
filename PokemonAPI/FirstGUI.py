from tkinter import *
from tkinter import ttk

root = Tk() #root widget

frame = ttk.Frame(root, padding = 10)

frame.grid()

ttk.Label(frame, text = "Hello World!").grid(column = 0, row = 0)
ttk.Button(frame, text = 'Quit', command=root.destroy).grid(column=1, row = 0)

root.mainloop()

# #create a label widget for display
# myLabel = Label(root, text = "Hello World")

# #push the label onto the screen
# myLabel.pack()

# root.mainLoop()