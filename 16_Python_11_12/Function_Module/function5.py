def checkPositive(num):
    if num>0:
        return True
    else:
        return False
def square(num):
    return num*num
def findFactorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    print("Factorial ",fact)

num=int(input("Enter number "))
print(checkPositive(num))
if checkPositive(num):
    print(square(num))
    findFactorial(num)
else:
    print(f"{num} is negative so can't perform square ")