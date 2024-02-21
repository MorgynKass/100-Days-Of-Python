# Number Guessing Game Objectives:
import random

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo

print(logo)

numbers = []
for n in range(101):
    numbers.append(n)

game_over = True

number = random.choice(numbers)
# print(number)

EASY_LEVEL = 10
HARD_LEVEL = 5

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty: 'easy' or 'hard'?\n")

if difficulty == "easy":
    number_guesses = EASY_LEVEL
    print(f"You have {EASY_LEVEL} attempts to guess the number.")
else:
    number_guesses = HARD_LEVEL
    print(f"You have {HARD_LEVEL} attempts to guess the number.")

while game_over:
    guess = int(input("Guess a number: \n"))
    if guess == number:
        print("Congrats! You guessed the number!")
        game_over = False
    elif guess < number:
        number_guesses -= 1
        if number_guesses == 0:
            print("Game Over, you ran out of attempts.")
            game_over = False
        else:
            print("Higher")
            print(f"You have {number_guesses} attempt/s left to guess the number.")
    else:
        number_guesses -= 1
        if number_guesses == 0:
            game_over = False
            print("Game Over, You lose.")
        else:
            print("Lower")
            print(f"You have {number_guesses} attempt/s left to guess the number")
