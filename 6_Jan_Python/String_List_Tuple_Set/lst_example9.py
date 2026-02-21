lst=[1,2,3,4,5]
ans=[]
# for i in lst:
#     ans.append(i**2)
# print(ans)
ans=[i**2 for i in lst]
print(ans)

lst_city=['ahemedabad','surat','rajkot']
lst_upper=[i.upper() for i in lst_city ]
print(lst_upper)

lst_len=[len(i) for i in lst_city]
print(lst_len)

# square of element if element is even
ans1=[]
# for i in lst:
#     if i%2==0:
#         ans1.append(i**2)
# print("Square of Even numbers ",ans1)

ans1=[i**2 for i in lst if i%2==0]
print("Square of Even numbers ",ans1)

# upper of city if city length is more then 5 letters 
ans2=[]
ans2=[i.upper() for i in lst_city if len(i)>5]
print(ans2)