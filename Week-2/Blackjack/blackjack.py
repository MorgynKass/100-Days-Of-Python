############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
# user_cards = []
# computer_cards = []

# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.

# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

from art import logo
import random

# Cards available to play with.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def play_game():
    print(logo)

    all_players_cards = {
        "users_cards": [],
        "computer's cards": [],
    }
    user = all_players_cards["users_cards"]
    computer = all_players_cards["computer's cards"]

    game_over = False

    def deal_card():
        """deals a card"""
        card = random.choice(cards)
        return card

    for c in range(2):
        user.append(deal_card())
        computer.append(deal_card())

    def calculate_score(hand):
        """calculates the sum/score of any cards in the argument"""
        if sum(hand) == 21 and len(hand) == 2:
            return 0
        if 11 in hand and sum(hand) > 21:
            hand.remove(11)
            hand.append(1)
        return sum(hand)

    def compare(user_score, computer_score):
        if user_score == computer_score:
            return "It's a draw."
        elif computer_score == 0:
            return "You lost, computer has a Blackjack."
        elif user_score == 0:
            return "You won with a Blackjack!"
        elif user_score > 21:
            return "You went over 21, you lose."
        elif computer_score > 21:
            return "Computer went over, you win!"
        elif user_score > computer_score:
            return "You win!"
        else:
            return "You lose."

    users_score = calculate_score(user)
    computers_score = calculate_score(computer)

    while not game_over:
        print(f"Your cards: {user} || current score: {users_score}")
        print(f"Computer's first card: {computer[0]}.")

        # Debugging
        # print(f"For debugging, Computer's Cards: {computer}")

        if users_score == 0 or computers_score == 0 or users_score > 21:
            game_over = True
        else:
            another_card = input("Type 'd' to draw another card or 'p' to pass.\n").lower()
            if another_card == "d":
                user.append(deal_card())
                users_score = calculate_score(user)
            else:
                game_over = True

    while computers_score != 0 and computers_score < 17:
        computer.append(deal_card())
        computers_score = calculate_score(user)

    print(f"Your final score was: {users_score}, your final hand was: {user}")
    print(f"Computer's final score was: {computers_score}, computer's final hand was: {computer}")
    print(compare(users_score, computers_score))


while input("Do you want to play a game of Blackjack?: y or n\n") == "y":
    play_game()
