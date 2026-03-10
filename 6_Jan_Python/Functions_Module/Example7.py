# create square function ,to return square of given list of numbers
# add these square into new list 
def square(number):
    return number*number

lst_sq=[]
lst_no=[1,2,33,55]
for i in lst_no:
    #print(square(i))
    lst_sq.append(square(i))

print(lst_sq)
