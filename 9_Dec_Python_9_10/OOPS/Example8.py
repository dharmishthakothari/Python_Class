class Employee:
    def __init__(self,eid,ename,salary):
        self.eid=eid
        self.ename=ename
        self.__salary=salary
    def __str__(self):
        return f"{self.eid} - {self.ename} - {self.__salary}"
e1=Employee(12,'dharmishtha',2300)        
print(e1)