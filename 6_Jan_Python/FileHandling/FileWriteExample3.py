lst_stmt=['\nThis is first stmt','\nThis is another stmt','\nThis is last stlt']
file=open("File2.txt","w")
file.writelines(lst_stmt)
print("Data Written Successfully")