#Canvas widget
from tkinter import *

class CanvasDemo:
    def __init__(self):
        window=Tk()
        window.title("Canvas demo")
        self.canvas=Canvas(window,width=200,height=100,bg="white")
        self.canvas.pack()
        frame=Frame(window)
        frame.pack()
    #Create rectangle
        btRectangle=Button(frame,text="Rectangle",command=self.displayRect)
        btRectangle.grid(row=1,column=1)
        #btRectangle.pack() can be used instead of grid window can be directly used instead of frame
    #Create Clear
        btClear=Button(frame,text="Clear",command=self.canvasClear)
        btClear.grid(row=2,column=2)
    #Create Oval
        btOval=Button(frame,text="Oval",command=self.displayOval)
        btOval.grid(row=1,column=2)
    #Create Arc
        btArc=Button(frame,text="Arc",command=self.displayArc)
        btArc.grid(row=1,column=3)
    #Create Line
        btLine=Button(frame,text="Line",command=self.displayLine)
        btLine.grid(row=1,column=4)
    #Create Polygon
        btPolygon=Button(frame,text="Polygon",command=self.displayPolygon)
        btPolygon.grid(row=1,column=5)
    #Create Text
        btString=Button(frame,text="String",command=self.displayString)
        btString.grid(row=1,column=6)        
        window.mainloop()

    def displayRect(self):
        self.canvas.create_rectangle(10,10,190,90,tags="rect")
    def displayOval(self):
        self.canvas.create_oval(10,10,190,90,tags="oval")
    def displayArc(self):
        self.canvas.create_arc(10,10,190,90,start=0,extent=180,width=2,fill="red",tags="arc")
    def displayLine(self):
        self.canvas.create_line(10,10,190,90,width=9,arrow="both",fill="blue",tags="line")
    def displayPolygon(self):
        self.canvas.create_polygon(10,10,190,10,30,50,fill="green",tags="polygon")
    def displayString(self):
        self.canvas.create_text(60,40,text="Hello this is Canvas",font="Times 8 bold underline",tags="string")
    def canvasClear(self):
        self.canvas.delete("rect","oval","arc","line","polygon","string")

CanvasDemo()
        

