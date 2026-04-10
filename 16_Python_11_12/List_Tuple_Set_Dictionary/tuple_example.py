# tpl=(1,2,3)
# print(tpl,type(tpl))
lst1=['India','France','Netherlands','Germany','Russia']
lst2=['Delhi','Paris','Amsterdam','Berlin','Moscow']
lst3=['India Gate','Effil tower','windmil','lake']
ans=list(zip(lst1,lst2,lst3))
#print(ans)
country,capital,place=zip(*ans)
print(country)
print(capital)
print(place)

