from tkinter import *

class ProcessButtonEvent:
    def __init__(self):
        window = Tk()
        label = Label(window,text="Welcome To Python")
        btOK=Button(window,text="OK",fg="red",command=processOK)
        btCancel=Button(window,text="Cancel",bg="yellow",command=processCancel)
        label.pack()
        btOK.pack()
        btCancel.pack()
        window.mainloop()

def processOK():
    print("OK Button is pressed")

def processCancel():
    print("Cancel button is clicked")

ProcessButtonEvent()

