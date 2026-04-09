lst=['Baroda','Surat','Ahmedabad']
update=input("Enter city you want to update ")
if update in lst:
    new_city=input("Enter new City ")
    
    index=lst.index(update)
    lst[index]=new_city
    print(f"Updated  List {lst}")
else:
    print(f"{update} city is not available in list" )
