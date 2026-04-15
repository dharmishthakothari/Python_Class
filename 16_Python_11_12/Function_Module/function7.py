def checkpositive(num):
    if num > 0:
        return True
    else:
        return False
def square(num):
    return num * num 
num=int(input("Enter a number: "))
print(checkpositive(num))
if checkpositive(num):
    print(square(num))
    #findfactorial(num) 
else:
    print(f"{num} is negative so can't per")