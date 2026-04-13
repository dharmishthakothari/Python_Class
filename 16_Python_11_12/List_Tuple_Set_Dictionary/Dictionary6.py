emp_data={
101:{"name":"Divya","email":"divya@gmail.com","salary":20000,"city":"Ahmedabad"},
102:{"name":"Vansh","email":"vansh@gmail.com","salary":20000,"city":"Baroda"},
103:{"name":"dharmishtha","email":"dharmishtha@gmail.com","salary":22000,"city":"Surat"},
104:{"name":"Dharati","email":"dharti@gmail.com","salary":20000,"city":"Ahmedabad"}
}
while True:
    print("1 Add Employee")
    print("2 Search Employee")
    print("3 Display All Employee")
    print("4. Update Employee ")
    print("5. Delete Employee")
    print("6. Search by Salary")
    print("7. Search by City ")    
    print("5. Exit")
    choice=int(input("Enter choice "))
    match choice:
        case 1:
            eid=int(input("Enter eid "))
            ename=input("Enter name ")
            email=input("Enter email ")
            salaray=int(input("Enter salary "))
            emp_data[eid]={"name":ename,"email":email,"salary":salaray}
            print("Employees addedd successfully ")
        case 2:
            search_id=int(input("Enter emp id "))
            if search_id in emp_data.keys():
                print(emp_data[search_id])
            else:
                print(f"{search_id} is invalid ")
        case 3:
            for k,v in emp_data.items():
                print(k)
                for k1,v1 in v.items():
                    print("\t",v1)
        case 4:
            search_id=int(input("Enter emp id "))
            if search_id in emp_data.keys():
                new_salary=int(input("Enter updated Salary "))
                emp_data[search_id]={"name":emp_data[search_id]["name"],"email":emp_data[search_id]["email"],"salary":new_salary}

            else:
                print(f"{search_id} is invalid ")
        case 5:break

