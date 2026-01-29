marks=int(input("Enter Marks "))
# if marks>=70 and marks<=100:
#     print("A")
# elif marks>=60 and marks<=69:
#     print("B")
# elif marks>=40 and marks<=59:
#     print("C")
# elif marks>=35 and marks<=39:
#     print("Pass")


match marks:
    case q if 70<= q <=100:print("A")
    #case range(70,100):print("A")
    case q if 60<= q <=69:print("B")
    case q if 40<= q <=59:print("C")
    case q if 35<= q <=39:print("pass")
    case _:print("Invalid Marks ")