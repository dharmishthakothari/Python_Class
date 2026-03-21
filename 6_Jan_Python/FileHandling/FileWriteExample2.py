file=open("File1.txt","w")

while True:
    data=input("Enter Data ")
    if data in ("END","end","End"):
        break
    file.write(data)
    file.write("\n")



print("Data Written Successfully")
file.close()