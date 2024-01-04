from datetime import datetime
# time = datetime(2024, 1, 1).date()
# print(time)


user = input("Enter a date: ")
y = 0
m = 0
d = 0

y = user[:4]
m = user[6:7]
d = user[9:10]

# time = datetime(y, m, d).date()
# print(time)
print(f"{y}-{m}-{d}")
