import re
name="Tops Technologies"
ans=re.search(r"s", name)
if ans:
    print(f"String found at {ans.start()}")
else:
    print("String does not found" )
