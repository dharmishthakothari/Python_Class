car_data ={"EV" : 
{ "Maruti" : {"Baleno" : [1200000,"xls"],"sCross":[2200000,"123"]},
    "Hundai":{"i10" : [100000,"grand"],"creata":[1890000,"190"]}

},

"Petrol":
{"Hundai" : {"i10" : [670000,"qqq"]}}

}     
# print(car_data)
# print(car_data["EV"]["Maruti"]["sCross"])
# print(car_data["Petrol"]["Hundai"])
company_name=input("Enter name of company ")
for i in car_data.keys():
    for j in car_data[i].keys():
        if j==company_name:
            print(i,"--->",car_data[i][j])
