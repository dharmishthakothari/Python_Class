import json
data={}
with open("studentDat.json","r") as file:
    data=json.load(file)

    print(data)
    