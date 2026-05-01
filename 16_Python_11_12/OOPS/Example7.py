class Person:
    def __init__(self,name,age,c_no):
        self.name=name
        self.age=age
        self.c_no=c_no
    def displayPerson(self):
        print(f"{self.name} - {self.age} - {self.c_no}")
class Employee(Person):
    def __init__(self, name, age, c_no,salary,dept):
        super().__init__(name, age, c_no)
        self.salary=salary
        self.dept=dept
    
    def displayPerson(self):
        super().displayPerson()        
        print(f"{self.salary} - {self.dept}")
e1=Employee('dharmistha',30,1234,43211,'Software')
e1.displayPerson()
