# declare class called Shape
class Shape:
    # create method calculateAread which return 0
    def calculateArea(self):
        return 0.0

#create a class Circle which extends Shape
class Circle(Shape):
    # create init method to initize radius
    def __init__(self,r):
        self.r=r
    # override calculateAread appy the logic to find area of circle 
    def calculateArea(self):
        return 3.14*self.r*self.r   

c1=Circle(2)
print(c1.calculateArea())