num=int(input("Enter no "))

for i in range(num):
    for j in range(num,i,-1):
        print("*",end=" ")
    print()