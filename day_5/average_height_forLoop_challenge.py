# This program is gonna calculates the average student height from a list of height.
# The average height can be calculated by adding all the heights together and dividing by the total number of heights.
# The average should be rounded to the nearest whole number e.g 120

# Prompt the user to enter the heights of students and turn them into a list
student_heights = input("Input a list of student heights.\n").split()
for item in range(0, len(student_heights)):
    student_heights[item] = int(student_heights[item])

print(student_heights)

# Calculate the sum of the height using for loop
total_height = 0
for height in student_heights:
    total_height += height

# Calculate the length of students using for loop
number_of_students = 0
for student in student_heights:
    number_of_students += 1

# Calculate the average height
average_height = round(total_height / number_of_students)
print(f"The average height of the students is {average_height}")