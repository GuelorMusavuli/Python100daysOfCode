from random import randint
from art import logo

# Global constants for the attempts(turns)
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Function to check user's guess against the actual answer
def check_answer(guess, answer, turns):
    """
    :param guess: user's guess
    :param answer: correct answer
    :param turns : turns
    :return: checks answer against guess. Returns the number of turns remaining.
    """
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")


# Function to set level difficulty
def set_difficulty():
    """
    :return:  set the number of attempts as per the level difficulty of the game
    """
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo)
    # Choosing a random number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    answer = randint(1, 100)
    # print(f"Pssst, the correct answer is {answer}")
    turns = set_difficulty()

    # Repeat the guessing functionality if they guess is wrong
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        # Let the user guess a number
        guess = int(input("Make a guess :"))

        # Track the number of turns and reduce by 1 if the guess is wrong
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return  # this prevent the user from continuing.
        else:
            print("Guess again.")


game()
