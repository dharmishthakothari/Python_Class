from abc import ABC,abstractmethod
class Vehical(ABC) :
    @abstractmethod
    def max_speed(self):
        print("Max speed is 0")
class Car(Vehical):
    pass
    # def max_speed(self):
    #     print("Max Speed is 120 K")
class Scooter(Vehical):
    def max_speed(self):
        print("Max Speed is 80 ")
obj=Car()
print("Car Max speed")
obj.max_speed()
objS=Scooter()
print("Scooter Max speed")
objS.max_speed()

