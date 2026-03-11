lst1=[1,2,3,4,33,"Devenshu",77,88,100,"Pratham"]
sum=0
# sum of each int element
for i in lst1:
    if type(i)==int:
        sum+=i
print(sum)