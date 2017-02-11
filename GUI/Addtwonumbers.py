from tkinter import *

def processAddition():
    print("Sum of " + str(num1.get()) + " and " + str(num2.get()) + " is " + str(num1.get()+num2.get())) 
window = Tk()
window.title("Adder")
frame1=Frame(window)
frame1.pack()
label1=Label(frame1,text="Enter First number:")
label2=Label(frame1,text="Enter Second number:")

num1=DoubleVar()
num2=DoubleVar()
entryNum1=Entry(frame1,textvariable=num1)
entryNum2=Entry(frame1,textvariable=num2)
Sum=Button(frame1,text="Add",command=processAddition)

label1.grid(row=1,column=1)
label2.grid(row=2,column=1)
entryNum1.grid(row=1,column=2)
entryNum2.grid(row=2,column=2)
Sum.grid(row=3,column=3)

window.mainloop()

