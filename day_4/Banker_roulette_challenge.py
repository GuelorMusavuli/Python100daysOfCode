# This program will select a random name from a list of names.
#  The person selected will have to pay for evrrybody's food bill.
import random

names_string = input("Give me everybody's names, separated by a comma.")

# Split the names into individual names and store them into a list
names = names_string.split(",")

# Get the total number of items in the list
num_items = len(names)

# Generate a random name from the list
random_choice = random.random(0, num_items - 1)

person_who_will_pay = names[random_choice]
# person_who_will_pay = random.choice(names)

print(person_who_will_pay + "is going to buy the meal today.")
