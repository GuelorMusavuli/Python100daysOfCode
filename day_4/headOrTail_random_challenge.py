# This a virtual coin program that will randomly tell the user "Heads"
# or "Tails" depending on the random number which was generated.
# The number can be either 0 or 1
import random

random_number = random.randint(0, 1)
if random_number == 1:
    print(f"Heads")
else:
    print(f"Tails")


