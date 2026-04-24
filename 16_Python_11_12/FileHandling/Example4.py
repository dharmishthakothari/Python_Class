with open("Second.txt","r") as file:
    # print(file.readline())
    # print(file.readline())
    # print(file.readline())
    # print(file.tell())
    file.seek(2)
    print(file.read())
    #print(file.tell())