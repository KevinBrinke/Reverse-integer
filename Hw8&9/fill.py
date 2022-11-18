#kevin brinke R01423368


from tkinter import *


class Options:
    def __init__(self):
        window=Tk()
        window.title("Radio buttons and check buttons")


        self.canvas= Canvas(window,width=300,height=70,)
        self.canvas.pack(padx=30,pady=5)

        frame1=Frame(window)
        frame1.pack(side=TOP)
        self.fillVar=IntVar()
        cbtFill=Checkbutton(frame1,text="Filled",variable=self.fillVar,command=self.fillcbt )
        cbtFill.pack(side=RIGHT)

        self.shape=IntVar()
        rbtOval=Radiobutton(frame1, text="Oval",variable=self.shape,value=1,command=self.makeOval)
        rbtOval.pack(side=RIGHT)
        rbtRectangle=Radiobutton(frame1, text="Rectangle",variable=self.shape,value=2,command=self.makeRectangle)
        rbtRectangle.pack(side=RIGHT)




        window.mainloop()

    def makeRectangle(self):
        print("This rectangle") 
        self.canvas.delete("shape")
        self.canvas.create_rectangle(10,10,290,60,tags="shape")
        if self.fillVar.get():
            self.canvas.create_rectangle(10,10,290,60,fill="Gray",tags=("filled"))
    def makeOval(self):
        print("This Oval")
        self.canvas.delete("shape")
        self.canvas.create_oval(10,10,290,60,tags="shape")
        if self.fillVar.get():
            self.canvas.create_oval(10,10,290,60,fill="Gray",tags=("filled"))

        
        
    def fillcbt(self):
        if self.fillVar.get()==1:
            print("filled")
            if self.shape.get()==1:
                self.makeOval()
            if self.shape.get()==2:
                self.makeRectangle()

        else:
            self.canvas.delete("filled")
            print("not filled")
Options()
