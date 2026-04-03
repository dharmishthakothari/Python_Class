num=int(input("Enter no "))

for i in range(num*2-1):
    if(i<num):
        for j in range(i,num):
            print("*",end=" ")
        print()
    else:
        #print((i-num)+2)
        for j in range((i-num)+2):
            print("*",end=" ")
        print()
