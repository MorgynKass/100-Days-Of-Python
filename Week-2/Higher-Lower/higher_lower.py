from art import logo, vs
from data import game_data
import random


def format_info(data):
    """Takes in data and pulls out the name, description, and country to then format into a comparison statement."""
    data_name = data["name"]
    data_description = data["description"]
    data_country = data["country"]
    return f"{data_name}, a {data_description}, from {data_country}"


def check_winner(guess, a, b):
    """Take the users guess as well as a and b's follower counts then returns if user is right."""
    if a > b:
        return guess == "a"
    else:
        return guess == "b"


def game():
    """The game"""
    print(logo)

    game_over = False

    data_b = random.choice(game_data)

    user_score = 0

    while not game_over:
        data_a = data_b
        data_b = random.choice(game_data)
        # Debugging data
        # print(data_a)
        # print(data_b)
        while data_a == data_b:
            data_b = random.choice(game_data)

        print(f"Compare A: {format_info(data_a)}")
        print(vs)
        print(f"Compare B: {format_info(data_b)}")
        user_choice = input("Who has more followers?: 'A' or 'B'\n").lower()

        followers_a = data_a["follower_count"]
        followers_b = data_b["follower_count"]
        # Debugging followers
        # print(followers_a)
        # print(followers_b)

        is_correct = check_winner(user_choice, followers_a, followers_b)

        if is_correct:
            user_score += 1
            print(f"You are correct! Your current score is: {user_score}")
        else:
            print(f"Game over. Your final score: {user_score}")
            game_over = True


game()
