from tkinter import *

window = Tk() # Parent container
label = Label(window,text="Welcome To Python")
button=Button(window,text="Click Me")
label.pack() #Place the label in window using pack manager
button.pack()
window.mainloop() # Create an event loop
