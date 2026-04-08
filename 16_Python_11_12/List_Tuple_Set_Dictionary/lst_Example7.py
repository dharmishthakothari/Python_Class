lst=[1,23,56,45,708]
print(f"{lst}")
# lst.clear()
# print(f"{lst}")
# del lst[2:4]
# print(f"{lst}")
# lst1=lst.copy()
# print(f"{lst1}")
# index_value=lst.index(708)
# print(f"{index_value}")
# print(f"{lst.count(708)}")
# #lst.remove(78)
# print(f"{lst}")
# lst.reverse()
# print(f"{lst}")
# lst.sort(reverse=True)
# print(f"{lst}")

lst_city=['Baroda','Surat','Rajkot','Ahmedabad','Mumbai']
lst_city.sort(key=len)
print(lst_city)
for i in range(len(lst_city)):
    print(i,"---->",lst_city[i])
