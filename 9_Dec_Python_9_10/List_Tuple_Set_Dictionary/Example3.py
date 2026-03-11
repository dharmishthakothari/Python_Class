#convert names into upper case from list
lst_name=['vivek','Nikunj','tufel','MIHIR','praTHAM']
for i in lst_name:
    print(i.upper())
print(lst_name)
#change names into upper in orginal list
print(lst_name[0])
for i in range(len(lst_name)):
    lst_name[i]=lst_name[i].upper()


print(lst_name)

