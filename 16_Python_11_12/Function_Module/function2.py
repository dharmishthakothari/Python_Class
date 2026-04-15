def studentDetails(rollNo,name,age):
    print(f"{rollNo} - {name} - {age}")

#studentDetails(11,"Shivam",20)
#studentDetails(12,"jay",20)
r=int(input("Enter roll no"))
n=input("Enter name ")
a=int(input("Enter age "))
studentDetails(r,n,a)