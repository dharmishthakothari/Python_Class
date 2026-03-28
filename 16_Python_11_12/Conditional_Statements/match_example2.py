age=int(input("Enter age "))
match age:
    case q if 0<=q<=2:
        print("infant")
    case m if 3<=m<=18:
        print("minor")
