from functools import reduce
def checkEven(num):
    if num%2==0:
        return num
# def square(num):
#     return num*num
# def sumSqare(a,b):
#     return a+b
list1=[1,2,6,3,8]
even_list=list(filter(checkEven,list1))
square_list=list(map(lambda no:no*no,even_list))
ans=reduce(lambda a,b:a+b,square_list)
print(ans)

def convert(cel):
    return (cel-32)*5/9
f=[12,23,11,34,56]
a=map(convert,f)
print(list(a))