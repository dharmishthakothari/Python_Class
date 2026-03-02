# name=input("Enter name ")

# first_por= name[0]
# last_po=name[len(name)-1]
# mid_por= name[1:len(name)-1]
# ans=last_po+mid_por+first_por
# print(name,ans)

name=str(input('ENTER THE NAME :-'))
part=name[2:7]
print(part)
for i in range(0,len(part)):   #start=0 , end= len(name) , step=2.
    print(part[i])