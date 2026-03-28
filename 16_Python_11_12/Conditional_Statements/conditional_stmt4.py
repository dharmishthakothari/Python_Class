age=int(input("Enter age "))
if age>=18:
    weight=int(input("Enter weight "))
    if weight>=55:
        print("User can donate blood")
    else:
        print("Due to underweight user can not donate blood")
else:
    print("Due to age user can not donate blood")