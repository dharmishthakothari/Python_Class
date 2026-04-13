class Distance:
   
    def __init__(self,feet,inch):
        self.feet=feet
        self.inch=inch
    def __str__(self):
        return f"{self.feet} - {self.inch}"
    def __add__(self, other):
        # d1.add(d2)
        # ans=Distance(0,0)
        # ans.feet=self.feet+other.feet
        # ans.inch=self.inch+other.inch
        # return ans
        return Distance(self.feet+other.feet,self.inch+other.inch)
    def __lt__(self, other):
        if self.feet<other.feet and self.inch<other.inch:
            return Distance(self.feet,self.inch)
        else:
            return Distance(other.feet,other.inch)
    
d1=Distance(2,23)
d2=Distance(12,23)
d4=Distance(2,2)

d3=Distance(0,0)

d3=d1+d2+d4
print(f"Addition of {d1} and {d2} is {d3}")
print(f"{d1<d2}")