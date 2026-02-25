
while True:
    print("1. Addition\n2. Substraction\n3. Multiplication\n4. Division\n5. Exit")
    choice=int(input("Please enter your choice "))
    match choice:
        case 1:
            no1=int(input("Enter number 1 "))
            no2=int(input("Enter number 2 "))
            print(f"Addition {no1+no2}")
        case 2:
            no1=int(input("Enter number 1 "))
            no2=int(input("Enter number 2 "))
            print(f"Substraction {no1-no2}")
      
        case 5: break
        case _:
            print("Enter valid choice")

if 1==2:
    pass
print(12)
def calculateSalary():
    #salary=12000*0.12
    pass