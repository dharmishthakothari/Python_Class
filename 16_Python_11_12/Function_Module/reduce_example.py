from functools import reduce
def add(a,b):
    return a+b
ans=reduce(add,[1,22,33,78,90])
print(ans)