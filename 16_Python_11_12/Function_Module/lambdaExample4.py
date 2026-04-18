lst_Student=['Shivam','Aatman','Jay']
lst_marks=[90,180,70]
lst_city=['Ahmedabad','Bhavnagar','Surat']
ans=list(zip(lst_Student,lst_marks,lst_city))
print("Original list ",ans)

ans.sort(key=lambda x:x[0])
print("Sorting by Name ",ans)

ans.sort(key=lambda x:x[1])
print("Sorting by marks ",ans)

ans.sort(key=lambda x:x[2])
print("Sorting by city ",ans)
