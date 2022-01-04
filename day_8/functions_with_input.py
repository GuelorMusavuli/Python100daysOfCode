# The passed in name is the parameter
def greet_with_name(name):
    print(f"Hello{name}")
    print(f"How do you do {name}")


# Here the actual value passed in
# is called an argument
greet_with_name("Peter")


# Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")


# Calling the function using positional arguments
greet_with("Jack Bauer", "London")

# Calling the functions using keyword arguments
greet_with(location="Kampala", name="John")
