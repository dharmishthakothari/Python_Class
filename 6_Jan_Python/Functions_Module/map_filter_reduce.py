# sum of square ,all even number
from functools import reduce
def evenNumber(num):
    if num%2==0:
        return num

lst=[1,2,3,4]

even_list=list(filter(evenNumber,lst))
square_list=list(map(lambda num:num*num,even_list))
ans=reduce(lambda x,y:x+y,square_list)
print(ans)

# with single stmt
ans=reduce(lambda x,y:x+y,list(map(lambda num:num*num,list(filter(evenNumber,lst))
)))
print(ans)
