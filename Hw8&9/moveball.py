#kevin brinke R01423368


from tkinter import *






class Move:

    def __init__(self):
        
        
        window= Tk()
        window.title("Moving ball")

        self.width = 400
        self.height= 300
        self.canvas= Canvas(window, bg="white", width= self.width, height= self.height)
        self.canvas.pack()
        self.x=50#creating ball size coordinants and distance per button(speed)
        self.y=50
        self.diameter=20
        self.speed=20

        frame=Frame(window)
        frame.pack()
        btLeft= Button(frame, text="Left", command=self.left)
        btLeft.pack(side=LEFT)
        btUp=Button(frame, text="Up", command=self.up)
        btUp.pack(side=LEFT)
        btDown= Button(frame, text="Down", command=self.down)
        btDown.pack(side=LEFT)
        btRight= Button(frame, text="Right", command=self.right)
        btRight.pack(side=LEFT)


        self.moving()

        window.mainloop()




    def left(self):
        for i in range (self.speed):#small increments of movement so it doesnt get denied movement early nor running partly off screen
            if self.x>2:
                self.x = self.x-2
        self.moving()
    
    def right(self):
        for i in range (self.speed):
            if self.x+self.diameter<self.width:
                self.x= self.x+2
        self.moving()
    
    def up(self): 
        for i in range (self.speed):
            if self.y>2:
                self.y= self.y-2
        self.moving()

    def down(self):
        for i in range (self.speed):
            if self.y+self.diameter<self.height:
                self.y= self.y+2
        #This is just me trying to create a slide instead of a 
        # for j in range (i):
        #     self.y+=self.speed/i
        self.moving()

    def moving(self):#redisplays the ball instead of creating multiple
        #self.canvas.after(100)
        #self.canvas.update()
        self.canvas.delete("ball")

        self.canvas.create_oval(self.x,self.y,self.x+self.diameter,self.y+self.diameter,fill="black", tags="ball")


        
            

Move()