set1={1,22,33,2,3}
set2={2,3,66,77,33}
# set3=set1.union(set2)
# print(set3)
set3=set1 | set2 | {77,88,2,3}
print(set3)
# set3= set1.intersection(set2)
# print(f"Intersection {set3}")
# set3= set1 & set2
# print(f"Intersection {set3}")

# set3=set2.difference(set1)
# print(f"Difference {set3}")

set3 = set2 - set1
print(f"Difference {set3}")

print(set3[2])