emp_data={
    "name":"divya",
    "age":20,
    "incentive":[120,2300,3000],
    "salary":23000
}
total_incentive=0
for k,v in emp_data.items():
    if type(v)==list:
        for i in v:
            total_incentive+=i

emp_data["inctotal"]=total_incentive
emp_data["totalsalary"]=emp_data["salary"]+emp_data["inctotal"]
print(emp_data)      
