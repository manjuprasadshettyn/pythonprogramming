# Dialog boxes

import tkinter.messagebox
#import tkinter.simpledialog
from tkinter import *

tkinter.messagebox.showinfo("Show Info", "This is an info message")
#Warning Message
tkinter.messagebox.showwarning("Show Warning","This is a warning")
#Error Message
tkinter.messagebox.showerror("Show Error","This is an error")
#Ask yes or no
isYes=tkinter.messagebox.askyesno("askyesno","Continue?")
print(isYes)
#Ask ok cancel
isOk=tkinter.messagebox.askokcancel("askokcancel","OK?")
print(isOk)
#Yes no Cancel
isyesnoc=tkinter.messagebox.askyesnocancel("askyesnocancel","Choice?")
print(isyesnoc)
# Simple Dialog
window=Tk()

name=tkinter.simpledialog.askstring("askstring","Enter your name")
print(name)

age=tkinter.simpledialog.askinteger("askinteger","Enter your age")
print(age)

weight=tkinter.simpledialog.askfloat("askfloat","Enter your weight")
print(weight)
