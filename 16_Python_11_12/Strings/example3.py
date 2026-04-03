c_no=int(input("Enter contact number  "))
c_no1=str(c_no)
if c_no1.startswith("91") and len(c_no1)==12:
    print(f"{c_no1} is valid contact number")
else:
    print(f"{c_no1} is invalid contact number")

