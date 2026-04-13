class Person:
    def __init__(self,name,c_no,address):
        self.name=name
        self.c_no=c_no
        self.address=address
    def display(self):
        print(f"{self.name} - {self.c_no} - {self.address}",end=" ")
class Employee(Person):
    def __init__(self, name, c_no, address,dept,salary):
        super().__init__(name, c_no, address)
        self.dept=dept
        self.salary=salary
    def display_emp(self):
        super().display()
        print(f"{self.salary} - {self.dept}")    

e=Employee("dharmishtha",123456,"paldi","Software",1234)
e.display_emp()
