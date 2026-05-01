class Student:
    def __init__(self,name,marks,c_no):
        self.name=name
        self.__marks=marks # marks is private data
        self.__c_no=c_no   # c_no is private data
    def __str__(self):
        return f"{self.name} - {self.__c_no} - {self.__marks}"

s1=Student('Divya',80,1234)
s1.__marks=20
print(s1)