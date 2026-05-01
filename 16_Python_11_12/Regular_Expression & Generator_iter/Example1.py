import re
ans=re.search('beatiful',"beatiful morning it is!!! is it beatiful")
#print(ans)
if ans:
    print("Available ",ans.start())
else:
    print("unavailable")

