
#Kevin Brinke R01423368
#Q1
#find area of pentagon


#input

import math

lengthVertex = eval(input("What is the length between the center of the pentagon and the vertex: "))

lengthSide = 2 * lengthVertex * (math.sin(math.pi/5))
print("The side lenth is: ",lengthSide)


#proccess
#I wasnt getting the correct outpiut for a pentagon with circumcircle radius with the area formula you provided
CONSTANT_PENTAGON_SIDE=(5*(5+2*(5**.5)**.5))/4  
areaPentagon = CONSTANT_PENTAGON_SIDE * lengthSide

#output
print("The area of the pentagon is: ",format(areaPentagon,".2f"))
