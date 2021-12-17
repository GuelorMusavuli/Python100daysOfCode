# This is a meme program that works out if a given number is an odd or even
# Even numbers can be divided by 2 with no remainder
# 86 is even or whole number because 86 + 2 = 43 which does not have any decimal places.

print("Welcome to odd or even calculator!")
number = int(input("Which number do you wanna check ?"))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
