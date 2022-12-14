from CircleGeometricObject import *
from RectangleGeometricObject import *

def main():
    circle = Circle(1.5)
    print("A circle", circle)
    print("The radius is", circle.getRadius())
    print("The area is:", circle.getArea())
    print("The Diameter is: ", circle.getDiameter())
    print("The Perimeter is: ", circle.getPerimeter())

    rectangle = Rectangle(2, 4)
    print("A rectangle", rectangle)
    print("The area is: ", rectangle.getArea())
    print("The perimeter us: ", rectangle.getPerimeter())

main()

    