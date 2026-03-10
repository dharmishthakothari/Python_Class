# create to check number is even /odd
def check_even(no):
    if no%2==0:
        #return "Even"
        return True
    else:
        #return "Odd"
        return False
def isEven(no):
    return no%2==0
print(check_even(10),isEven(10))
print(check_even(101),isEven(101))

