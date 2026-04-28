class Employee:
    def __init__(self,eid,ename,salary,dept):
        self.eid=eid
        self.ename=ename
        self.salary=salary
        self.dept=dept
    def display(self):
        print(f"{self.eid} - {self.ename} - {self.salary} - {self.dept}")

e1=Employee(101,'dharmishtha',10000,'software')       
e2=Employee(102,'Heeya',12000,'Finance')
e3=Employee(103,'Deepak',15000,'HR')
#Book - class - isbnNo , title , auther , no_of_pages
#5 objects 


e2.display()