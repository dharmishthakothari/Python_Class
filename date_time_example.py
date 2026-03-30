import datetime
print(datetime.date.today())
print(datetime.date.today().month)

print(datetime.datetime.now())
cur_datetime=datetime.datetime.now()
print(cur_datetime.strftime("%d-%m-%Y %H:%M"))

