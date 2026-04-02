import math
start_no=int(input("Enter start no "))
even_odd=input("Even/Odd?")
no_of_iteration=int(input("Enter Range "))
j=2
ans1=0
if even_odd=='Even':
    j=2
else: 
    j=1
for i in range(0,no_of_iteration):
    print(start_no,"-",j,"-",math.factorial(j))
    ans=start_no/math.factorial(j)
    print(ans)
    ans1+=ans
    j+=2
    start_no+=20
print(ans1)