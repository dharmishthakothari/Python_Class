class Distance:
    # feet and inch 
    def __init__(self,feet,inch):
        self.inch=inch
        self.feet=feet
    
    def __str__(self):
        return f"{self.feet} - {self.inch}"

    def __add__(self,other):
        ans=Distance(0,0)
        ans.feet=self.feet+other.feet
        ans.inch=self.inch+other.inch
        return ans
    def __mul__(self,other):
        return Distance(self.feet*other.feet,self.inch*other.inch)

    def __eq__(self,other):
        if self.feet>other.feet and self.inch>other.inch:
            return True
        else:
            return False

d1=Distance(91,21)
print(d1)

d2=Distance(9,2)
print(d2)

d3=Distance(1,2)
print(d3)


d4=d1+d2+d3
print(d4)

d5=d1*d2
print(f"Multilication of {d1} and {d2} is {d5}")

print(d1==d2)