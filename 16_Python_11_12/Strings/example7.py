name=input("Enter name ")
# for i in name:
#     print(i)
# index thru 
count=0
for i in range(len(name)):
    #print(i,"--->",name[i])
    if name[i]=='a':
        count+=1

print(f"Count of a is {count}")