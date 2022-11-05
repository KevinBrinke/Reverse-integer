#Kevin Brinke r01423368
#Rectangle test
from rectangleclass import Rectangle

def main():
    width= 4  #eval(input("sepcify width"))
    height= 40  #eval(input("Specify height"))


    width2= 3.5  #eval(input("sepcify width"))
    height2=  35.7 #eval(input("Specify height"))
    
    r1=Rectangle(height,width)
    r2=Rectangle(height2,width2)
    print(width,"widthR1")
    print(height,"heightR1")
    print(r1.getArea(),"area1")
    r1.setHeight(32)
    print(r1.getPerimeter(),"perim1\n")
    print(width2,"widthR2")
    print(height2,"heightR2")
    print(format(r2.getArea(),".2f"),"area2")
    print(r2.getPerimeter(),"perim2")

    r3= Rectangle()
    print(r3.getArea())
    



main()

