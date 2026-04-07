import re
msg="This is python class"
#ans=re.findall(r"\d+",msg)
ans=re.findall(r"\w+",msg)
print(len(ans))
ans=re.findall(r"\b\w{4}\b",msg)
print(ans)

ans=re.findall(r"\W{4}",msg)
print(ans)
ans=re.findall(r"\s{4}",msg)
print(ans)
ans=re.findall(r"\S{4}",msg)
print(ans)