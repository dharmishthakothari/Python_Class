from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def getArea(self):
        return 0.0
class Rectagle(Shape):
    # def getArea(self):
    #     return 23
    def greet(self):
        print("Good Afternoon")
r=Rectagle()
print(r.getArea())