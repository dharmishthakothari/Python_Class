lst1=[1,2,3,4]
lst2=[('Shivam', 90, 'Ahmedabad'), ('Aatman', 180, 'Bhavnagar'), ('Jay', 70, 'Surat')]
print(max(lst1))
ans=max(lst2,key=lambda i:i[1])
print("Max  ",ans)