#Kevin Brinke R012423368
#recctangle class 





class Rectangle:
    def __init__(self,height=2,width=1):

        self.height=height
        self.width= width

    
    def getArea(self):
        return  self.height * self.width
    
    def getPerimeter(self):
        return (2*self.height+2*self.width)


    def setHeight(self, heightChange):
        self.height=heightChange


