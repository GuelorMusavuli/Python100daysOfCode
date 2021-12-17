import random

# generate a random integer between a and b(both of those numbers inclusive): random(a,b)
random_integer = random.randint(1, 10)
print(random_integer)

# generate a random decimal number between 0 and 1 but 1 non inclusive
random_float = random.random()
print(random_float)

# generate a random decimal number between 0 and 5
randomFloat = random.random() * 5
print(randomFloat)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")
