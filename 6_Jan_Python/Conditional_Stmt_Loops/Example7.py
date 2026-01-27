age=int(input("Enter age "))
weight=int(input("Enter weight "))
if age>18:
    if weight>50:
        print("User is eligible to donate blood")
    else:
        print("Due to under weight user can not donate blood ")
else:
    print("Not eligible to donate blood")
    
