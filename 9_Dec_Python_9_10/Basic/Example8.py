month_name=input("Enter Month Name ")
if month_name in ["January","March","May","July","August","Octomber","December"]:
    print("31 days")
elif month_name in ["February"]:
    print("28/29 days")
elif month_name in ["April","June","September","November"]:
    print("30 days")
else:
    print("Invalid Month Name ")
