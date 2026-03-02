name=input("Enter name")

print(name)
# character by charancter 
for i in name:
    print(i)

#thru index 
print("Lenght of String is ",len(name))
print("Second letter from string ",name[2])

for i in range(len(name)):
    print(i,name[i])

# print alternate letters from string
print("Alternate letters from string")
for i in range(0,len(name),2):
    print(i,name[i])