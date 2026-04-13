student_data = {
  "std1":{"name": "divyansh","c_no": "12345","marks": [20,20,30]},
   "std2":{"name": "shivam","c_no": "12356","marks": [120,20,400]},
   "std3":{"name": "vansh","c_no": "12357","marks": [220,20,30]},
   "std4":{"name": "ansh","c_no": "12358","marks": [120,20,40]}
}
for k,v in student_data.items():
    print(k)
    #for k1,v1 in v.items():
    #print("in-----",student_data[k]["marks"])
    student_data[k]["totalmarks"]=student_data[k]["marks"][0]+student_data[k]["marks"][1]+student_data[k]["marks"][2]
print(student_data)