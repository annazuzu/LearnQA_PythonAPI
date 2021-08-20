import datetime
timestamp = "1629444855"

# Gives you the date and time in local time
d = datetime.datetime.fromtimestamp(int(timestamp))
print(d.strftime("%d.%m.%y %H:%M:%S"))