name=input("Enter name ")
i=name.count("a")
print(f"{name} contains {i} is word")
print(f"Total string length is {len(name)}")
ans=name.split()
print(len(ans))

for i in ans:
    print(f"{i}--->{i.count('a')}")
