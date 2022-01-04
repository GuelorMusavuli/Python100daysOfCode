# You're painting a wall. The instructions on the paint can says that
# 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall,
# calculate how many cans of paint will be needed to buy.
# number of cans = (wall height x wall width) / coverage per can.
# The result should be rounded up to a whole number.
from math import ceil


def paint_calc(height, width, cover):
    area = height * width
    number_of_cans = ceil(area / cover)
    print(f"You'll need {number_of_cans} cans of paint")


test_h = int(input("Height of wall:"))
test_w = int(input("Width of wall:"))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
