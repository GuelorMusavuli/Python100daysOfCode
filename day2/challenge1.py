# Prompt the user to enter two digit numbers
two_digit_number = input("Type a two digit number ")

# Check the type of two-digit-number
print(type(two_digit_number))

# Get the first and second digits using subscripting then convert string to int
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

# Sum the two digits and displays the result
print("The sum of the two numbers is " + str(first_digit + second_digit))
