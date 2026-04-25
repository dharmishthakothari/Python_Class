import json
student_data={
    "name":"Nandini",
    "age":20,
    "subject":"Python"
}
with open("data.json","w") as file:
    json.dump(student_data,file)
    print("Data Written Successfully ")
