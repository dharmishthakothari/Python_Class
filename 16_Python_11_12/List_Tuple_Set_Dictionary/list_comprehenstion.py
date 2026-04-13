lst=[1,2,3,4]
# lst_sq=[]
# for i in lst:
#     lst_sq.append(i*i)
lst_sq={i*i for i in lst}
print(lst_sq)

lst_city=["ahmedabad","surat","baroda"]
upp_lst_city=[i.upper() for i in lst_city if len(i)>5]
print(upp_lst_city)