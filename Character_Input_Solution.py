import datetime as dt

current_time = dt.datetime.now()

year = current_time.strftime('%Y')						# Get current year
year = int(year)

name = input("What's your name: ")
age = input("How old are you: ")
y100 = year + 100 - age									# Calculate the year when getting 100 years old

print(name + " you will turn 100 years old in the year " + str(y100))
