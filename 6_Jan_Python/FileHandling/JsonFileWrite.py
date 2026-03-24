import json
student_data={
"name":"Mahesh",
"age":20,
"address":"Paldi",
"course":"python"
}
with open("studentData.json","w") as file:
    json.dump(student_data,file)
    print("Data addedd into file ")