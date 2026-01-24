age=int(input("Enter Age "))
if age>=0 and age<=2:
    print("Infant")
elif age>2 and age<=18:
    print("minor")
elif age>=19 and age<=50:
    print("Adult")
elif age>=51 and age<=70:
    print("Seniour")
elif age>=71:
    print("Super Seniuor")
else:
    print("Age is invalid")