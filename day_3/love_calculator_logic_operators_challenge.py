# This program is gonna test the compatibility between two people.
# We're gonna use the super scientific method recommended by BuzzFeed.
# It will tak both two people's names and check for the number of time the letters in word TRUE occurs.
# Then checks for the number of times the letters in the word LOVE occurs. T
# Then combine these numbers to make a 2 digit number.
# For love scores less than 10 or > 90, the message should be : "Your score is x, you go together like coke and mentos"
# For love scores between 40 and 50, the message should be : "You are alright together"
# Otherwise, the message should be : "Your score is z"
print("Welcome to the Love calculator")
name1 = input("What is your name ?")
name2 = input("What is their name ?")

combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90) :
    print(f"Your love score is {love_score}, you go together like coke and mentos")
elif 40 <= love_score <= 50:
    print(f"Your love score is {love_score}, You are alright together")
else:
    print(f"Your score is {love_score}")

