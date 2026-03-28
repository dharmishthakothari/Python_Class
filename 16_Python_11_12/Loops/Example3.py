num=int(input("Enter number "))
if num%2==0:
    for i in range(1,11):
        print(f"{num} * {i} = {num*i}")
else:
    print("Multilication not perform ")