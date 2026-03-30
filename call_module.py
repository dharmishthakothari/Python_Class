# import Logical_operation
# num=int(input("Enter number "))
# print(f"Sum of Digit is {Logical_operation.sumOfDigit(num)}")
# print(f"Count no of Digit is {Logical_operation.findNoOfDigit(num)}")

from Logical_operation import sumOfDigit,checkDivisableBy5
num=int(input("Enter number "))
print(f"Sum of Digit is {sumOfDigit(num)}")
print(f"Number is divisable by 5 {checkDivisableBy5(num)}")
