from CircleGeometricObject import Circle
from RectangleGeometricObject import Rectangle

def main():
    c = Circle(4)
    r = Rectangle(4, 4)
    displayObject(c)
    displayObject(r)
    print("Are the circle and rectangle the same size?", isSameArea(c, r))

def displayObject(g):
    print(g.__str__())

def isSameArea(g1, g2):
    return g1.getArea() == g2.getArea()

main()
