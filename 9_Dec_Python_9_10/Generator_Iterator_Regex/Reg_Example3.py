import re
# name=input("Enter String ")
# ans=re.findall(r"[A-Z]{3,7}",name)
# print(ans)
lst=['91-9090909012','81-1234567890','2187271212','My contact number is 9876543211']
for i in lst:
    if re.search(r"\d{2}-\d{10}",i):
        print(f"{i} is valid contact number ")