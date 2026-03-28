age=int(input("Enter age "))
if age>=0 and age<=105:
    if age>=0 and age<=2:
        print("infant")
    elif age>=3 and age<=18:
        print("minor")
    elif age>=19 and age<=50:
        print("Adult")
    elif age>=51 and age<=70:
        print("Seniur")
    elif age>=71 and age<=105:
        print("Super Senior")
else:
    print("Invalid Age")