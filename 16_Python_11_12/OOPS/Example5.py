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
    
    def displayEmp(self):
        self.displayPerson()
        print(f"{self.salary} - {self.dept}")

class Student(Person):
    pass # marks , grade

e1=Employee('dharmishtha',30,12345,12345,'software')
#e1.displayPerson()
e1.displayEmp()