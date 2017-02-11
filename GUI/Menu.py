#Menu
from tkinter import *
class MenuDemo:
    def __init__(self):
        window=Tk()
        window.title("Menu Demo")
        menubar=Menu(window)
        window.config(menu=menubar)
        operationMenu=Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Operation",menu=operationMenu)
        operationMenu.add_command(label="Add",command=self.add)
        operationMenu.add_command(label="Subtract",command=self.subtract)
        operationMenu.add_separator()
        operationMenu.add_command(label="Multiple",command=self.multiply)
        operationMenu.add_command(label="Division",command=self.division)

        exitMenu=Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Exit",menu=exitMenu)
        exitMenu.add_command(label="Quit",command=window.quit)

        frame1=Frame(window)
        frame1.pack()
        label1=Label(frame1,text="Enter First number:")
        label2=Label(frame1,text="Enter Second number:")
        result=Label(frame1,text="Result:")

        self.num1=DoubleVar()
        self.num2=DoubleVar()
        self.num3=DoubleVar()
        entryNum1=Entry(frame1,textvariable=self.num1)
        entryNum2=Entry(frame1,textvariable=self.num2)
        entryNum3=Entry(frame1,textvariable=self.num3)
        label1.grid(row=1,column=1)
        label2.grid(row=2,column=1)
        result.grid(row=3,column=1)
        entryNum1.grid(row=1,column=2)
        entryNum2.grid(row=2,column=2)
        entryNum3.grid(row=3,column=2)
        
        window.mainloop()

    def add(self):
        self.num3.set(self.num1.get()+self.num2.get())
    def subtract(self):
        self.num3.set(self.num1.get()-self.num2.get())
    def multiply(self):
        self.num3.set(self.num1.get()*self.num2.get())
    def division(self):
        self.num3.set(self.num1.get()/self.num2.get())

MenuDemo()
        
