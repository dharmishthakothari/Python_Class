import re
# msg=input("Enter String ")
# ans=re.findall("python",msg)
# print(ans)

msg=input("Enter String ")
#ans=re.findall(r"\d+",msg)
ans=re.findall(r"\d{10}",msg)
print(ans)