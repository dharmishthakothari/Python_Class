class Shape:
    def getArea(self):
        return 0
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def getArea(self):
        return self.length*self.width

class Square(Shape):
    pass

shape=Shape()
print(f"Area of shape is {shape.getArea()}")
r=Rectangle(2,3)
print(f"Area of Rectangle {r.getArea()}")

s=Square()

print(f"Area of Square {s.getArea()}")
