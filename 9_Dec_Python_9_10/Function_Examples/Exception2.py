import traceback
try:
    num=int(input("Enter number "))
    print(num)
    dict1={"name":"dharmishtha"}
    print(12/2)

    print(dict1["name"])
    file=open("sdf","r")
except ValueError as v:
    print(v)
except ZeroDivisionError as z:
    print(z)
except Exception as e:
    
    print(e)
    traceback.print_exc()
else:
    print("In else")
