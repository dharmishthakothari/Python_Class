lst_numbers=[23,12,45.34,'adasd',45,90]
total=0
for i in lst_numbers:
    if type(i)==int:
        total+=i
print(total)