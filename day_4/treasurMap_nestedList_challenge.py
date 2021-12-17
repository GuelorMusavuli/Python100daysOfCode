# This is a program which wil make a spot with an X.
# The map is made of 3 rows of blank squares.
# It should allow users to enter the position of the treasure using two-digit system.
# The first digit is the vertical column number and the second digit is the horizontal row number.
# example column 2 and row 3 would be entered as 23.
print("Welcome to the Treasure Map!")

row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
map_rows = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you wanna put the treasure ?")

horizontal = int(position[0])
vertical = int(position[1])

map_rows[vertical - 1][horizontal - 1] = "X"
print(f"{row1}\n{row2}\n{row3}")

