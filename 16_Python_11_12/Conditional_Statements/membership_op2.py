month=input("Enter Month ")
if month in ("April","June","September","November"):
    print(f"{month} contains 30 days ")
elif month in ("January","March","May","July","August","Octomber","December"):
    print(f"{month} contains 31 days ")
elif month=='February':
    print(f"{month} contains 28/29 days ")
else:
    print(f"{month} invalid ")