def studentDetails(**kwargs):
    for k,v in kwargs.items():
        print(k,v)



studentDetails(id=11,name='Riya',address='Paldi')
studentDetails(id=12,name='Netra',address='CGRoad',age=20)
studentDetails(id=13,address='CGRoad',age=20,name='Mahesh')