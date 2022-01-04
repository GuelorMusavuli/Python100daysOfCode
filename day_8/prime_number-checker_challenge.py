# Prime numbers are numbers that can only be cleanly divided by itself and 1.
# Write a function that checks whether the number passsed into it is a prime number or not

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False

    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")


n = int(input("Input the number to check :"))
prime_checker(number=n)
