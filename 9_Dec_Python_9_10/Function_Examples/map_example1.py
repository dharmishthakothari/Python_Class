def square(num):
    return num*num

lst1=[1,2,3,4]
# sq_list1=[]
# for i in lst1:
#     sq_list1.append(square(i))

sq_list1=list(map(square,lst1))
print(sq_list1)

cube_list3=list(map(lambda x:x**3,lst1))
print(cube_list3)

lst_city=['ahmedabad','jamnagar']
upper_city=list(map(str.upper,lst_city))
print(upper_city)