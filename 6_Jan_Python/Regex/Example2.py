import re
msg="contact number is 9876543212 my house number is 12 and pincode is 765432 and another cotact number is 1234567890"
#ans=re.findall(r"\d+",msg)
ans=re.findall(r"\d{6,10}",msg)
print(ans)