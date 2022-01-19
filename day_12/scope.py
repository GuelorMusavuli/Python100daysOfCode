# The scope applies not only to variable by anything that is maned, hence Namespace

# Global scope (at the top level)
enemies = 1
player_health = 10

# Global scope can be incredibly useful when it comes to defining constants.
# Constants are immutable variable. And to differentiate it from a mutable variable,
# Python's naming conventions recommend to turn it into uppercase
PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@guelor_musavuli"


def increase_enemies():
    enemies = 2  # This is local scope(within  a function)
    print(f"enemies inside function : {enemies}")


increase_enemies()
print(f"enemies outside function : {enemies}")


def game():
    def drink_portion():  # function at local scope

        # The following code explicitly modify the global variable
        # player_health within a function, however it's not a good practice
        # as it's confusing and prone to creating bug.
        # We could instead return it as the output of the function (return player_health += 10),
        # and then make use of it any where in the code or either assign it to a variable.
        global player_health
        player_health += 10
        portion_strength = 2

        print(player_health)

    drink_portion()


game()

# There is no Block Scope in Python
if 3 > 2:
    variable = 10  # This makes no sense
