age=int(input("Enter age "))
if age>18:
    learning_licence=input("Do you have a learning licence? (y/Y)")
    if learning_licence=='y' or learning_licence=='Y':
        print("User is eligible for licence")
    else:
        print("First use has to apply for learning licence")
else:
    print("User is not eliglble for licence")
