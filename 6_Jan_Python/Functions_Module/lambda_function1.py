add=lambda x,y,z:x+y+z
print(add(20,30,10))

# create function which calcualte square of number
# def square(n):
#     return n*n
square=lambda x:x**2
lst1=[1,2,3]
lst2=[]
for i in lst1:
    lst2.append(square(i))
print(lst2)

ans=lambda num:"Even" if num%2==0 else "Odd"
print(ans(561))
# for i in lst1:
#     print(ans(i))

