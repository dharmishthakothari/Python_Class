# remove first and last element without using function
# with single statement
lst_city=['Mumbai','Surat','Ahmedabad','Kolkata','Rajkot','Pune','Hydarabad','Jaipur']
size=len(lst_city)
del lst_city[1:size-1]
print(lst_city)