# This program will determine whether a given year is a leap year.
# A normal year has 365 days.Leap years instead have 366, with an extra day in February.
# The work is done on every year that is evenly divisible by 4
# except every year that is evenly divisible by 100, unless the year is also evenly divisible by 100.

print("Welcome to leap year detector!")
year = int(input("Which year do you wanna check ?"))

# Is it cleanly divisible by 4
if year % 4 == 0:
    # is it cleanly divisible by 100
    if year % 100 == 0:
        # is it cleanly divisible by 400
        if year % 400 == 0:
            print("This is a leap year.")
        else:
            print("Not a leap year.")
    else:
        print("This is a leap year")
else:
    print("Not a leap year")


