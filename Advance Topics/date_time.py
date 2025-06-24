import datetime 
date = datetime.date(2025,1,2)
today = datetime.date.today


time = datetime.time(12,30,0) # hours -> munite -> second


print(date)
print(today)


now = datetime.datetime.now()
now = now.strftime("%H:%M:%S %d-%m-%Y")
print("Current date : ",now)

target_datetime = datetime.datetime(2020,1,2,12,30,1)
current_time = datetime.datetime.now()

if target_datetime < current_time:
    print("Target has been passed")
else:
    print("You still have time")