def checkEven(num):
    if num%2==0:
        return num

lst1=[1,11,23,36,78]
# create even number list from given list
# lst_even=[]
# for i in lst1:
#     lst_even.append(checkEven(i))
# print(lst_even)
lst_even=filter(checkEven,lst1)
print(list(lst_even))