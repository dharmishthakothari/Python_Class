def factorial(n):
    # fact=1
    # for i in range(1,n+1):
    #     fact*=i
    # return fact
    if n==1:
        return 1
    else:
        print("else ",n)
        return n * factorial(n-1)    
    

print(factorial(7))