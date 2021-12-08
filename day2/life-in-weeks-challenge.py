# This program is created to apply the skills about math operations.
# It typically tell the user how many days, weeks, months are left
# if he/she lives until 90 years old. It will take their current age as input
# and ouput a message with their time left in the following format :
# "You have x days, y weeks, and z months left." where x,y, and z are replaced
# with the actual calculated numbers. The output should match the words in
# the example output precisely, also the results should be rounded to the closet whole number.
# Note that, there are 365 days, 52 weeks, and 12 months in a year.
# Prompt the user's age
age = input("What is your current age ? ")
age_until_90 = 90 - int(age)
days_until_90 = age_until_90 * 365
weeks_until_90 = age_until_90 * 52
months_until_90 = age_until_90 * 12

message = f"You have {days_until_90} days, {weeks_until_90} weeks, and {months_until_90} months left."
print(message)