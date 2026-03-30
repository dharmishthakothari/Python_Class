def isEven(num):
    return num%2==0

def checkDivisableBy5(num):
    if num%5==0:
        return num

def findNoOfDigit(num):
    count=0
    while(num!=0):
        rem=num%10
        count+=1
        num=num//10
    
    return count

def sumOfDigit(num):
    sum=0
    while(num!=0):
        rem=num%10
        sum+=rem
        num=num//10
    return sum