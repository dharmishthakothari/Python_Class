dict1={
    "riya@gmail.com":["Riya",20,"C G road",120] ,
      "kavya@gmail,com":["Kavya",20,"Nikol",190],
      "kunal@gmail.com":["Kunal",22,"S G Highway",230]
      }
#fetch value from key
# print(dict1["kunal@gmail.com"])
sum=0
for i in dict1.values():
    # #print(i[3])
    # if i[3]>150:
    #     print(i)
    sum+=i[3]
    
print(sum)
