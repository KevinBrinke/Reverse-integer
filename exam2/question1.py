#Kevin Brinke

import math

class RegularPolygon:
    def __init__(self,nInput=3,sideInput=1,xInput=0,yInput=0):
        self.__n=nInput#number of sides
        self.__side=sideInput#length
        self.__x=xInput#x coordinate for center of polygon
        self.__y=yInput#y coord

        self.area= (self.__n*self.__side**2)/(4*math.tan(math.pi/self.__n ))
        self.perimeter=self.__n*self.__side


    def setSideCount(self,nSetter):
        self.__n=nSetter
    def getSideCount(self):
        return self.__n

    def setSideLength(self,sideSetter):
        self.__side=sideSetter
    def getSideLength(self):
        return self.__side

    def setxCenterCoordinate(self,xSetter):
        self.__x=xSetter
    def getxCenterCoordinate(self):
        return self.__x
        
    def setySideLengthCenterCoordinate(self,ySetter):
        self.__x=ySetter
    def getyCenterCoordinate(self):
        return self.__y


    def getArea(self):
        return self.area

    def getPerimeter(self):
        return self.perimeter
