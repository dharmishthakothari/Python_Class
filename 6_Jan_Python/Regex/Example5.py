import re
lst_email=['test@gmail.com','werwer','test123@gmail.com','234ewe@23sdfin']

pattern = r"^\S+@\S+\.\S+$"
for i in lst_email:
    ans=re.search(pattern,i)
    print(ans)