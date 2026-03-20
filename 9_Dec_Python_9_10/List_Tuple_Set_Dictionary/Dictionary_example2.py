# store details of 5 students in dictionary 


# Mihir --25 -- CGRoad --mihir@gmail.com,70
# Avani --20 -- Bhavnagar--avani@gmail.com,65
student_details={
"pratham@gmail.com":["Pratham",22,"Paldi",90],
"harmi@gmail.com":["Harmi",20,"Navaragpura",89],
"mihir@gmail.com":["Mihir",25,"CGRoad",70]
}
for k,v in student_details.items():
    print(k)
    for i in v:
        print("\t",i)