from tkinter import *

class RotatingMessage():
    def __init__(self):
        window=Tk()
        window.title=("Rotating message")
        window.geometry("400x200")

        frame=Frame(window)
        frame.pack()
        text=StringVar()
        text.set("Programming is fun")
        labelText=Label(frame, textvariable=text,font=("Ariel",15))
        labelText.pack(pady=85)
        click=


        def setText2(self):
            text.set("it is fun to program")
        def setText1(self):
            text.set("Programming is fun")
            

        






        window.mainloop()
RotatingMessage()