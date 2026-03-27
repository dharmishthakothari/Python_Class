from functools import reduce
def sumNo(no1,no2):
    return no1*no2

lst1=[i for i in range(1,11)]
ans =reduce(sumNo,lst1)
print(ans)