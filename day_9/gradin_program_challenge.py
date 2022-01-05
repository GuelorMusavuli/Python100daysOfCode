"""Assume we have access to a DB of student_scores in the format of a dictionary. The 'keys' in student-scores are
the 'names' of the students and the 'values' are their exam scores. This program challenge is gonna converts
their scores to grades. By the end of the program, there should be a new dictionary called 'student_grades' that should
contain student names for keys and their grades for values. The final version of the student_grades dict will be checked.
This is the scoring criteria :
    Scores 91-100 : Grade = "Outstanding"
    Scores 81-90 : Grade = "Exceeds Expectations"
    Scores 71-80 : Grade = "Acceptable"
    Scores 70 or lower : Grade = "Fail"
"""

student_scores = {
    "John": 81,
    "Maurice": 78,
    "Peter": 99,
    "Victor": 74,
    "Nathan": 62

}
# Create an empty dict
student_grades = {}

# Add the grades to student_grades dict
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

# Print the the grades
print(student_grades)
