import re
msg="This is beatiful morning"
msg1="beatiful morning it is beatiful"
ans=re.search(r"beatiful$",msg1)
#print(ans)
if ans:
    print("String is available in message")
else:
    print("String is unavailable in message")
# msg1="beatiful morning it is"
# ans1=re.match("beatiful",msg1)
# print(ans1)