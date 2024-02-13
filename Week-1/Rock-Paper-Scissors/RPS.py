import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

rps = [rock, paper, scissors]

choice = int(input("Rock, Paper, or Scissors?: 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

if choice > 2:
    print("You typed in an invalid number.")
else:
    output = rps[choice]
    print(f"You Chose: \n {output}")

    computer_choice = random.randint(0, len(rps)-1)
    computer_output = rps[computer_choice]
    # print(computer_choice)
    print(f"Computer Chose: \n {computer_output}")

    if choice == 0 and computer_choice == 2:
        print("You win!")
    elif choice == 2 and computer_choice == 0:
        print("You lose.")
    elif computer_choice > choice:
        print("You lose.")
    elif computer_choice < choice:
        print("You win!")
    else:
        print("It's a draw")
