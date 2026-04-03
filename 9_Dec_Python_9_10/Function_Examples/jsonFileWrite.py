import json
data={
"name":"Mihir",
"subject":"Python",
"email":"mihir@gmail.com",
"age":25
}
with open("studentData.json","w") as file:
    json.dump(data,file)
    print("Data written Successfully ")