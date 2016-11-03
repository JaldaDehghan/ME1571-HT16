from datetime import datetime

str_time = str(datetime.now().time())
print("It's " + str_time)

hours = str_time[:2]

hours = int(hours)

if hours >= 5 and hours <=8:
    print("Good morning")
elif hours >= 9 and hours <= 12:
    print("Good day")
elif hours >= 13 and hours <= 17:
    print("Good afternoon")
elif hours > 17 and hours <= 24:
    print("Good night")
else:
    print("Ooops, it's past midnight. Go to sleep")
