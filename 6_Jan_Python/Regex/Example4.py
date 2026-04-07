import re
name="Tops Technologies"
ans=re.search(r"Tops", name)
print(ans.group())