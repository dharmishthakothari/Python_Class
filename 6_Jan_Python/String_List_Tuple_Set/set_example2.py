set1={1,2,3,4,5}
set2={1,2,33,44,55,66}
# set3=set1.union(set2)
# print(set3)
# set3=set1.intersection(set2)
# print(set3)
# set3=set1.difference(set2)
# print(set3)
# set3=set2.difference(set1)
# print(set3)
# set1.add(44)
# print(set1)

set3 = set1 & set2 & {1,3,55,33}
print(set3) 

set3 = set1 | set2
print(set3)

set3=set1-set2
print(set3)

