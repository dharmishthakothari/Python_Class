number=int(input("Enter number "))
for i in range(2,number):
    if number%i==0:
        print(f"{number} is not prime")
        break
else:
    print("Number is prime ")
