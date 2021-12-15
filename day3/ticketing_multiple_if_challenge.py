print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm ?"))
bill = 0  # initialize bill amount

# nested condition using comparison operators
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age ?"))

    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif 45 >= age <= 55:  # age <= 45 and age <=55
        print("Everything is gonna be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")

    # This action is checked on each of the above conditions
    wants_photo = input("Do you wanna a photo taken ? Y or N.")
    if wants_photo == "Y":
        bill += 3  # add $3 on each one bill.

    # displays the total amount of bill
    print(f"Your final bill is {bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")