# This program will interprets the Body Mass Index based on a user's weight and height.
# It will tell them the interpretation of the BMI based on the BMI value under certain conditions
print("Welcome to the BMI Calculator 2.0")
height = float(input("Enter your height in m : \n"))
weight = float(input("Enter your weight in kg : \n"))

# Calculate BMI
body_mass_index = round(weight / height ** 2)

# Checks BMI value for interpretations
if body_mass_index < 18.5:
    print(f"Your height is {height} m, your weight is {weight} kg,")
    print(f"and your body mass index is {body_mass_index}. You are underweight.")
elif body_mass_index < 25:
    print(f"Your height is {height} m, your weight is {weight} kg,")
    print(f"and your body mass index is {body_mass_index}. You have an normal weight.")
elif body_mass_index < 30:
    print(f"Your height is {height} m, your weight is {weight} kg,")
    print(f"and your body mass index is {body_mass_index}. You are overweight.")
elif body_mass_index < 35:
    print(f"Your height is {height} m, your weight is {weight} kg,")
    print(f"and your body mass index is {body_mass_index}. You are obese.")
else:
    print(f"Your height is {height} m, your weight is {weight} kg,")
    print(f"and your body mass index is {body_mass_index}. You are clinically obese.")
