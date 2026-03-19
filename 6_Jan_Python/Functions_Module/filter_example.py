def evenNumber(num):
    if num%2==0:
        return num

lst1=[1,2,33,44,55]
even_list=list(filter(evenNumber,lst1))
print(even_list)