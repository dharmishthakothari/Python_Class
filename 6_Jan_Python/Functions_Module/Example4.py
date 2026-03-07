# create function to perfrom addition and subtraction
# if addition of 2 numbers is more then 100 then do subtraction 
def addition(no1,no2):
    return no1+no2
    

def subtraction(no1,no2):
    print("Subtraction is ",no1-no2)

no1=int(input("Enter number 1 "))
no2=int(input("Enter number 2 "))

ans=addition(no1,no2)
print("Addition is ",ans)
if ans>=100:
    subtraction(no1,no2)
