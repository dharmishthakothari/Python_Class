# create square function ,to return square of given list of numbers
# add these square into new list 
def square(number):
    return number*number

lst_no=[1,2,33,55]
# for i in lst_no:
#     #print(square(i))
#     lst_sq.append(square(i))

lst_sq=list(map(square,lst_no))
print(lst_sq)

#with lambda
lst_no1=list(map(lambda num:num*num,lst_no))
print("With lambda ",lst_no1)
list_city=['baroda','surat','ahmedabad']
upper_city=list(map(str.upper,list_city))
print(upper_city)

lst_base=[1,2,3,4]
lst_pow=[2,2,2]
# 1^2 2^2 3^2 4^1

ans=list(map(pow,lst_base,lst_pow))
print(ans)
