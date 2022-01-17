"""
Blackjack is a game that is played using card. The goal of the game is for
the user(Dealer) to add up their card up to the largest number without going over 21.
If the cards in the user's hand add up to more than 21, then it could be a 'Bust',
meaning the user loses instantly, and it does not matter how much they've gone over 21.
As long as it is over 21, then the user loses. The way that the cards are counted is that,
all the cards from 2 to 10 count as their saved value. So a 6 is 6, 4 is 4 etc.
But the Jack(J) Queen(Q) and King(K), each counts 10. Another special card is A, which can either be
counted as 1 to the total or it can be counted as an eleven. And depending on whether it should go over 21
or under 21, we can decide which value A we want to represent.
"""
import random
import os
from art import logo

"""
  ##### Our Blackjack House Rules  #####

   The deck is unlimited in size.
   There are no jokers.
   The Jack/Queen/King all count as 10.
   The the Ace can count as 11 or 1.
   Use the following list as the deck of cards:
   cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
   The cards in the list have equal probability of being drawn.
   Cards are not removed from the deck as they are drawn.
   The computer is the dealer."""


def deal_card():
    """ Returns a random card from the deck of cards."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    """ Take a list of cards and return the score calculated from the cards."""
    score = sum(cards)

    # Check for a blackjack (a hand with only 2 cards : Ace(11) + 10),
    # then it is a blackjack, represented by 0
    if score == 21 and len(cards) == 2:  # or 11 in cards and 10 in cards and len(cards) == 2:
        return 0
    # check for an Ace(11), and if the score is already over 21,
    # then remove the Ace and replace it with a 1
    elif 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)

    return score


def compare(user_final_score, computer_final_score):
    """Take both final user's score and the computer's score, compare them,and return the decision."""

    # If both the user and the computer are over, then they lose.
    # If the computer and user both have the same score, then it's a draw.
    # If the computer has a blackjack (0), then the user loses.
    # If the user has a blackjack (0), then the user wins.
    # If the user_score is over 21, then the user loses.
    # If the computer_score is over 21, then the computer loses.
    # If none of the above, then the player with the highest score wins.
    if user_final_score > 21 and computer_final_score > 21:
        return "You went over. You lose 😤"
    elif user_final_score == computer_final_score:
        return "Draw 🙃"
    elif computer_final_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_final_score == 0:
        return "Win with a Blackjack 😎"
    elif user_final_score > 21:
        return "You went over. You lose 😭"
    elif computer_final_score > 21:
        return "Opponent went over. You win 😁"
    elif user_final_score > computer_final_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():

    print(logo)

    # Deal both the user and computer a starting hand of 2 random cards each.
    user_cards = []
    computer_cards = []
    is_game_over = False
    user_score = 0
    computer_score = 0
    for card in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Let the user to keep playing or drawing cards
    # by rechecking the score with every new card drawn until the game ends
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards:{user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        # If the computer or the user has a blackjack (0)
        # or if user's score is over 21, then the game ends.
        # Otherwise, ask the user if they wanna draw another card
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            if input("Type 'y' to get another card, type 'n' to pass: ") == "y":
                user_cards.append(deal_card())  # draw new card to the former one
            else:
                is_game_over = True

    # Let the computer to keep drawing cards as long as its score is less than 17,
    # once the user is done playing the game.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        # Recalculate the pc's score to get updated and while is evaluated on the latest score
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand :{user_cards}, final score: {user_score}")
    print(f"    Computer's final hand :{computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


def clear():
    """Clear the console after each game."""
    os.system('cls')


# play_game()

""" Ask the user if the want to restart the game. 
If yes, clear the console and start a new game of blackjack."""

while input("Do you wanna play a game of Blackjack ? Type 'y' or 'n': ") == "y":
    clear()
    play_game()
