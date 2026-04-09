lst=['Baroda','Surat','Ahmedabad']
# Baroda --- 3
# Surat --- 2
# Ahmedabad ---4
count=0
for i in lst:
    count=0
    for i1 in i:
        if i1 in ('a','A','E','e','i','I','O','o','U','u'):
            count+=1
    print(i,'--->',count)

