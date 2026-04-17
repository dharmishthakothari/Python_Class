def findEven(num):
    if num%2==0:
        return num
def square(num):
    return num*num
lst_number=[1,11,12,13,14]
ans=list(filter(findEven,lst_number))
sq_list = list(map(square,ans))
print(sq_list)