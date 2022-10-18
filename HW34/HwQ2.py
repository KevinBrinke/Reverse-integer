#Kevin Brinke R01423368
#Q2
#Draw olypic rings in turtle

import turtle

#input
radius=eval(input("For the Olypmic rings please enter the radius of your choice: "))
distanceVert= (radius*2)
distanceHori= 2 * radius - (radius/10)
count=0
#process
turtle.dot(10,"red")
turtle.pensize(15)
turtle.penup()
turtle.forward(-distanceHori)
while count < 5 :
    turtle.pendown()
    if count == 0:
        turtle.color("blue")
    if count == 1:   
        turtle.color("black")
    if count == 2:   
        turtle.color("red")
    if count == 3:   
        turtle.color("green")
    if count == 4:   
        turtle.color("yellow")
    
    turtle.circle(radius)
    turtle.penup()
    if count == 2:
        turtle.home()
        turtle.forward(1.5*distanceHori)
        turtle.right(90)
        turtle.forward(-distanceVert/2)
        turtle.left(-90)

    turtle.forward(distanceHori)
    count += 1



turtle.done()