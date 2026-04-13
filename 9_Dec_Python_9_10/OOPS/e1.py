class rectangle():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length* self.breadth
    
    def __add__(self,other):
        return rectangle(self.length+ other.length,self.breadth+other.breadth)
r1=rectangle(20,5)
print(r1.area())
r2=rectangle(30,10)
print(r2.area())
r3=rectangle(40,20)
print(r3.area())
r4=r1+r2+r3
print(r4)