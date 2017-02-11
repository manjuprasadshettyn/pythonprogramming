from tkinter import *

def processCheckbutton():
    print("Checkbutton is" + ("Checked" if v1.get()==1 else "Unchecked"))

def processRadiobutton():
    print("Red" if v2.get()==1 else "Yellow")

def processButton():
    print("Your Name is "+ name.get())
    
window = Tk()
window.title("Widgets Demo")

#Frame1
frame1=Frame(window)
frame1.pack()

# Checkbutton
v1=IntVar()
cbtbold=Checkbutton(frame1,text="Bold",variable=v1,command=processCheckbutton)
cbtbold.grid(row=1,column=1)

#Radio button
v2=IntVar()
rbRed=Radiobutton(frame1,text="red",bg="red",variable=v2,value=1,command=processRadiobutton)
rbYellow=Radiobutton(frame1,text="yellow",bg="yellow",variable=v2,value=2,command=processRadiobutton)
rbRed.grid(row=1,column=2)
rbYellow.grid(row=1,column=3)

#Frame2 label, entry, button,message
frame2=Frame(window)
frame2.pack()
label=Label(frame2,text="Enter your name:")

name=StringVar()
entryName=Entry(frame2,textvariable=name)
btGetName=Button(frame2,text="GetName",command=processButton)
message=Message(frame2,text="It is a widgets demo")

label.grid(row=1,column=1)
entryName.grid(row=1,column=2)
btGetName.grid(row=1,column=3)
message.grid(row=1,column=4)

# add text
text=Text(window)
text.pack()
text.insert(END,"Tip: \nThe best way to learn Tkinter is to read")
text.insert(END," these carefully designed examples and use them")

window.mainloop()
