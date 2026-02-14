name=input("Enter name ")
ans = name[-1] + name[1:len(name)-1] + name[0]
print(f"Original string {name} and output is {ans}")