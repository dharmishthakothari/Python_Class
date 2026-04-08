lst_city=['Baroda','Surat','Rajkot','Ahmedabad','Mumbai']
c_name=input("Enter city ")
# if lst_city.count(c_name)>0:
#     print(f"{c_name} is available in list")
# else:
#     print(f"{c_name} is unavailable in list")

#Second
# if c_name in lst_city:
#     print(f"{c_name} is available in list")
# else:
#     print(f"{c_name} is unavailable in list")

#Third
for i in lst_city:
    if i==c_name:
        print(f"{c_name} is available in list")
        break
else:
    print(f"{c_name} is unavailable in list")