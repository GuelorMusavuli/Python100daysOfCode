
# This program calculates the Body Mass Index from a user's weight and height
# It's found by dividing a person's weight(in kg)
# by the square of their height(in m).

print("Welcome to the BMI Calculator")
height = input("Enter your height in m : \n")
weight = input("Enter your weight in kg : \n")

# Calculate BMI
body_mass_index = int(int(weight) / float(height) ** 2)

# print the result using f-string
print(f"Your height is {height} m, your weight is {weight} kg, and your body mass index is {body_mass_index}.")





