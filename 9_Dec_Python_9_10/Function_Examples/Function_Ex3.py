def checkNumber(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"

print(checkNumber(230))
lst1=[1,23,45,66]
for i in lst1:
    print(i,checkNumber(i))