print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm ?"))

# nested condition using comparison operators
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age ?"))
    if age < 12:
        print("Please pay $5 tickets.")
    elif age <= 18:
        print("Please pay $7 tickets.")
    else:
        print("Please pay $12 tickets.")
else:
    print("Sorry, you have to grow taller before you can ride.")