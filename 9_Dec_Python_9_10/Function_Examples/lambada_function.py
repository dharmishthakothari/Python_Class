add=lambda x,y:x+y
print(add(12,23))

square=lambda x:x**2
print(f"Square {square(12)}")

lst1=[1,2,3,4]
for i in lst1:
    square=lambda x:x**2
    print(f"Square {square(i)}")
    