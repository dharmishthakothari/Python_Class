class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    # def display(self):
    #     print(f"{self.x}:{self.y}") 
    def __str__(self):
        return f"{self.x}:{self.y}"
    def __add__(self, other):
        p3=Point(0,0)
        p3.x=self.x+other.x
        p3.y=self.y+other.y
        return p3
    
    def __sub__(self, other):
        p3=Point(0,0)
        p3.x=self.x-other.x
        p3.y=self.y-other.y
        return p3
p1=Point(2,45)
p2=Point(4,67)
print(p1)
print(p1)
p3=Point(0,0)
p3=p1+p2
print(p3)
p3=p1-p2
print(p3)
