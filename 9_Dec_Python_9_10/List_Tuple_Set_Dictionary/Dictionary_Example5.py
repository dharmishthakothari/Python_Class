dict1={i:i*i for i in range(1,11)}
print(dict1)
city_names=['ahmedabad','baroda','surat','rajkot']
# city name as key
# value is as upper case of city
dict_city={i:i.upper()+'-'+str(len(i)) for i in city_names}
print(dict_city)
