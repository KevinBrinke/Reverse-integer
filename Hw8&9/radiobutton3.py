from tkinter import *

#i cannot figure out for the life of me how to do the color on the buttons properly, 
# dont know how to return a value and set it without it constantly setting it to white
class RadioButtons:
    def __init__(self,):
        self.window=Tk()
        self.window.title("Radio buttons and buttons")
    #frame radio button background colors
        self.frame1= Frame(self.window)
        self.frame1.pack()
        self.color=StringVar()
        self.color.set("White")
    
    #color radio buttons
        rbRed = Radiobutton(self.frame1, text="Red", variable=self.color, value="Red", command = self.processRadiobutton)
        rbRed.pack(side=LEFT)
        rbYellow = Radiobutton(self.frame1, text="Yellow", variable=self.color, value="Yellow", command = self.processRadiobutton)
        rbYellow.pack(side=LEFT)
        rbWhite = Radiobutton(self.frame1, text="White", variable=self.color, value="White", command = self.processRadiobutton)
        rbWhite.pack(side=LEFT)
        rbGray = Radiobutton(self.frame1, text="Gray", variable=self.color, value="Gray", command = self.processRadiobutton)
        rbGray.pack(side=LEFT)
        rbGreen = Radiobutton(self.frame1, text="Green", variable=self.color, value="Green", command = self.processRadiobutton)
        rbGreen.pack(side=LEFT)
        
        

        
    #end color radio buttons
    
        self.width = 300 # Width of the canvas
       
        self.welcomeCanvas= Canvas(self.window, width = 300, height = 50)
        self.welcomeCanvas.pack()
        self.dx=20
        self.x=0
         # Starting x position
      

        self.welcomeCanvas.create_text(self.x, 30, 
            text = "Welcome",font=("arial",20), tags = "text")

        frame2=Frame(self.window)
        frame2.pack()
        btLeft=Button(frame2, text="<=",command=self.movetextcanvasleft)
        btLeft.pack(side=LEFT)
        btRight=Button(frame2, text="=>",command=self.movetextcanvasright)
        btRight.pack(side=LEFT)
        

              
        



        self.window.mainloop()
    def movetextcanvasright(self):
        if self.x < self.width:
            self.welcomeCanvas.move("text",self.dx,0)
            self.x+=self.dx
    def movetextcanvasleft(self):
    
        if self.x > 0:
            self.welcomeCanvas.move("text",-(self.dx),0)
            self.x-=self.dx
        

    def processRadiobutton(self):
        print(self.color.get())
        self.window.configure(bg=self.color.get())
        self.welcomeCanvas.configure(bg=self.color.get())


        
    
        
RadioButtons()


#i cannot figure out for the life of me how to do the color on the buttons properly, 
# dont know how to return a value and set it without it constantly setting it to white