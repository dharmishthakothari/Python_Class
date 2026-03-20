emp_details={
    "emp101":
    {"name":"Pratham","age":20,"salary":20000,"dept":"Software"},
    "emp201":
    {"name":"Mihir","age":20,"salary":15000,"dept":"Finance"},
"emp301":
{"name":"Devanshu","age":22,"salary":22000,"dept":"Software"},
"emp401":
{"name":"Harmi","age":20,"salary":17000,"dept":"HR"},
}

#display those employees whose salary is more then 20000

for k,v in emp_details.items():
    # v is dictionary here 
    if emp_details[k]["salary"]<20000:
       #print(k,v)
       print(k,emp_details[k]["name"],emp_details[k]["age"])
        

#display those employee whose empid is selected/entered 
emp_id=input("Enter emp id ")
dict1=emp_details[emp_id]
for k,v in dict1.items():
    print(k,'---->',v)

#display those employee who works in software department
# display those employees who works in department enterd by user 

#display those employee whose age is more then 25
