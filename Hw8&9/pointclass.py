#kevin brinke R01423368

class Point:
    def __init__(self,x=0,y=0,pointNumber=0):
        self.__x=x
        self.__y=y
        self.pointNumber=str(pointNumber)
    def getx(self):
        return self.__x
    def gety(self):
        return self.__y
        
    
    def distance(self,p1):
        return ((self.__x-p1.getx())**2 + (self.__y- p1.gety())**2)**(1/2)
        
        
    
    def isNearBy(self,p1,p2):
        if p1.distance(p2) <= 5 :
            return True
        return False
        
    def __str__(self):
        return f'p{self.pointNumber}{self.__x,self.__y}'


def main():
    x1,y1,x2,y2=eval(input("Enter x1, y1, x2, y2: "))
    p1=Point(x1,y1,pointNumber=1)
    p2=Point(x2,y2,pointNumber=2)
    print("Points ",p1.__str__()," and ", p2.__str__())
    print("The distance between the two points is:",p1.distance(p2))
    if p2.isNearBy(p1,p2):
        print("The two points are near eachother")
    else:
        print("The two points are not near eachother")
    

main()