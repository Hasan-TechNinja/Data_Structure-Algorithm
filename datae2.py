from datetime import datetime
user = input("Enter a date: ")
dateArray = user.split("-")

validDate = datetime(int(dateArray[0]),int(dateArray[1]),int(dateArray[2])).date()
print(validDate)
t = type(validDate)
print(t)