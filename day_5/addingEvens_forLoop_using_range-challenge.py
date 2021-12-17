# This program calculate the sum of all the even numbers from 1 to 100
# Including 1 and 100.
total_evens = 0
for number in range(1, 101):
    if number % 2 == 0:
        total_evens += number
print(total_evens)

# alternative
total = 0
for number in range(1, 101, 2):
    total += number
print(total)
