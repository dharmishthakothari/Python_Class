def isPrime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True

def countDigit(num):
    count=0
    while(num!=0):
        rem=num%10
        count+=1
        num=num//10
    return count

def isEven(num):
    pass