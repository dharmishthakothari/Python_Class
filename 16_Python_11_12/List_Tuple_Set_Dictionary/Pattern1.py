num=int(input("Enter no "))
for i in range(num):
    #print("row ",i)
    for j in range(0,i+1):
        #print("\tcol ",j)
        #print("$",end=" ")
        print(chr(65),end=" ")
    print()