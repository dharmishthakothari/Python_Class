# def personDetails(*args):
#     print("Person Details ")
#     for i in args:
#         print("\t",i)
def personDetails(name,*args):
    print(name)
    for i in args:
        print("\t",i)
personDetails("dharmishtha",40,"Ahmedabad","Python")
personDetails("Devanshu","Rajkot","Data Science")
personDetails("harmi","Python")
personDetails("Pratham",20,"Data Science","Good Student",200,"A Grade")

