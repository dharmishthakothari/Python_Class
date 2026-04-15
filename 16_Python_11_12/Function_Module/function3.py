def checkNumber(num):
    if num%2==0:
        print("Even")
    else:
        print("Odd")
def findFactorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    print(fact)

# n=int(input("Enter number "))
# checkNumber(n)

n1=int(input("Enter number "))
findFactorial(n1)