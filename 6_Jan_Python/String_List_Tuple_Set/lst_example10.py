lst_number=[1,2,3,4,33,67]
# lst_ans=[i**2 for i in lst_number if i%2==0]

# print even if no is even else print odd
ans=["Even" if i%2==0 else "odd" for i in lst_number]
print(ans)

#calculate square of no if number is even else calculate cube
ans2=[i**2 if i%2==0 else i**3 for i in lst_number]
print(ans2)

# covernt city name into upper if lenth of city is more then 5 leeter else convert into lower
