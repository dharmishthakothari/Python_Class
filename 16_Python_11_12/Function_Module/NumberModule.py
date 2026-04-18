def checkPositive(num):
    if num>0:
        return num
def checkEven(num):
    if num%2==0:
        return True
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact