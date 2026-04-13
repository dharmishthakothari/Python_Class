class Student:
    def __init__(self,name,c_no):
        self.name=name
        self.__c_no=c_no
    def __str__(self):
        return f"{self.name} - {self.__c_no}"
    def getC_no(self):
        return self.__c_no
    def setC_no(self,contact_no):
        self.__c_no=contact_no


# class Engineer:

#     def display(self):
#         s=Student("Dharmishtha" , 23233)        
#         print(s.name,s.__c_no)
# e=Engineer()
# e.display()
s=Student("Dharmishtha" , 23233)        
print(s)    
s.setC_no(90909)
print(s)    
print(s.getC_no())