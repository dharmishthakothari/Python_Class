#Factorial of given number
num=int(input("Enter number "))
ans=1
#for i in range(num,0,-1):
for i in range(1,num+1):
    ans=ans*i
    

print(f"Factorial of {num} is {ans}")