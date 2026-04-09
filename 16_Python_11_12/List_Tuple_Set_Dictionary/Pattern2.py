num=int(input("Enter no "))
for i in range(num*2-1):
    #print("row ",i)
    if i<num:
        for j in range(i,num):
        #print("\tcol ",j)
            print("*",end=" ")
        
    else:      
        for j in range(i-num+2):
            print("*",end=" ")
    print()