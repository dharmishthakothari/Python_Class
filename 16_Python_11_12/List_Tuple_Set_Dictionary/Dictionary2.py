student_data={
"name":"Nandini",
"email":"nan@gmail.com",
"specialize":"Software",
"Subject":['Programming in C','C++','Python']
}
for k,v in student_data.items():
    
    if type(v)==list:
        print(k)
        for i in v:
            print("\t",i)
    else:
        print(k,'\t',v)