
#s=lambda num:num*num
s1=lambda base,power:base**power
lst=[1,2,3]
for i in lst:
    #print(s(i))
    s=lambda i:i*i
    print(f"{s(i)}")
print(s1(2,5))