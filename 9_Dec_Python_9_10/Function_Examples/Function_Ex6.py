def personDetails(**kwargs):
    #print(kwargs)
    # for i in kwargs.keys():
    #     print(i)
    print(kwargs['name'],kwargs['subject'])


personDetails(name="Dharmishtha",age=30,subject="python")
personDetails(name="Pratham",subject="Data Science",remarks="Regular")
personDetails(name="Mihir",subject="Data Analytics",remarks="Working")
