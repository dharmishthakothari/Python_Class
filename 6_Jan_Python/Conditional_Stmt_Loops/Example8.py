age=int(input("Enter age "))
license=input("Do user have Learning Licence ??? ")
if age>18:
    #if license=="yes" or license=="YES":
    if license in("yes","YES"):
        print("User is eligible for license")
    else:
        print("User is not eligible for license , user doesn't have learning license")
else:
    print("User is not adult so not eligble for licence")