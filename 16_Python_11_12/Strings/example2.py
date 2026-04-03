email=input("Enter email ")
# check email address is valid or not
if email.endswith("@gmail.com"):
    print(f"{email} is valid email address")
else:
    print(f"{email} is invalid email address")