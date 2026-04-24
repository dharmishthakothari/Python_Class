file=open("Second.txt","w")

while True:
    data=input("Enter data ")
    if(data=='END'):
        break
    file.write(data+"\n")
