#find square of numbers and add it into another list
lst_number=[1,22,3,4,5]
lst_sq=[]
lst_qube=[]
for i in lst_number:
    lst_sq.append(i**2)
    lst_qube.append(i**3)

print(lst_sq)
print("Cube of lst ",lst_qube)

# from list find only even numbers and add it into another list
lst_even=[]
for i in lst_number:
    if i%2==0:
        lst_even.append(i)
    
print("Even list is ",lst_even)