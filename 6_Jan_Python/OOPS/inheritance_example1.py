class Person:
    def __init__(self,name,c_no,address):
        self.name=name
        self.c_no=c_no
        self.address=address
    def display(self):
        print(f"{self.name}-{self.c_no}-{self.address}")

class Student(Person):
    def __init__(self, name, c_no, address,roll_no,marks):
        super().__init__(name, c_no, address)
        self.roll_no=roll_no
        self.marks=marks
    def displayStudent(self):
        print(f"{self.roll_no}-{self.name}-{self.address}-{self.c_no}-{self.marks}")

class CollegeStudent(Student):
    pass
class Company:
    pass
class Employee(Student,Company):
    pass

obj=Student("Kunal",1234,"Paldi",23,200)
obj.displayStudent()

obj1=Student("Mahesh",2232,"CGRoad",45,220)
obj1.displayStudent()