import random
from hangman_words import word_list
from hangman_art import stages, logo

# Randomly choose a word from the word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Keep track of the number of lives left and the game
end_of_game = False
lives = 6

# Print the logo at the start of the game
print(logo)

# Create blanks represented by "_" for each letter in the chosen word
display = []
for letter in range(word_length):
    display.append("_")  # or display += "_"

# Let the user guess again until the user has guessed all the letters in the chosen word
# and ''display' has no more blanks ("_"). Then tell the user they've won.
while not end_of_game:
    # Ask the user to guess a letter in the chosen word.
    guess = input("Guess a letter :").lower()

    # If the user has typed a letter they've already guessed,
    # print it and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")

    # Loop through each position in the chosen word;
    # If the letter at that position matches 'guess' then reveal
    # that letter in the display at that position.i.e. check if
    # the letter user guessed is one of the letters in the chosen_word.
    # e.g. If the user guessed "a" and the chosen word was "java",
    # then display should be ["_", "a", "_", "a"]
    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position}\n"
              f" Current letter: {letter}\n"
              f" Guessed letter: {guess}")
        if guess in letter:  # letter == guess
            display[position] = letter  # set the item at the current position to letter

    # Check if user is wrong,
    # i.e. if letter is not in the chosen word
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win!")

    # Print the ASCII art from 'stages' that corresponds
    # to the current current number of 'lives' the user has remaining.
    print(stages[lives])