with open('Example3.py','r') as file:
    data=file.read()
with open('first.txt','w') as file2:
    file2.write(data)
    print("Data Copied successfully ")