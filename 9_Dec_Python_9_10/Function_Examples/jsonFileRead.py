import json
with open("studentData.json","r") as file:
    data=json.load(file)
    #data=file.read()
    print(type(data))
    print(data)

