name=input("Enter Name ")
print(name.capitalize())
print(name.title())
print(name.upper())
print(name.count("is"))
print(name.find("is"))
#print(name.index("is"))
# for i in range(len(name)):
#     print(i,'---->',name[i])
if name.count("a")>=1:
    print(f"{name} contains a letter")
else:
    print(f"{name} doesn't contains a letter")

print("With method 2")
for i in name:
    if i=='a':
        print(f"{name} contains a letter")
        break
else:
    print(f"{name} doesn't contains a letter")

ans=name.split(maxsplit=2)
print(ans)