print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# Write your code below this line 👇

road = input("You've been walking down a dirt road for quite awhile now. Finally you reach a sign that reads: Left "
             "towards Dark Forest, Right towards Gloomy Beach. Do you go Left or Right\n").lower()
if road == "right":
    beach = input("You decided to take the road to the beach. When you arrived you noticed a pier that led into the "
                  "ocean. At the end sat a small boat with a figure sitting inside. The figure asks if you'd like a "
                  "ride. Do you go? Yes or No\n"
                  "").lower()
    if beach == "yes":
        island = input("You spend some time on the boat with the figure, finally you reach a small island "
                       "covered with fog. You walk to the beach and read a sign that says: Follow the Mountain Trail "
                       "for riches or Follow the Woods for knowledge. Do you go Mountain or Woods?\n"
                       "").lower()
        if island == "woods":
            end = int(input("You follow the wooded trail and eventually reach a spring. There is a sign that asks for "
                            "a number. What is your number?\n"))
            if end <= 50:
                print("The spring pities you for not asking for more, 50 golden coins appear at your feet.")
            elif end <= 100:
                print("The spring is quite happy with your amount, 100 golden coins appear at your feet.")
            else:
                print("The spring thinks you are too greedy, you are swallowed up and never to be seen again.")
        else:
            print("The Mountain trail leads to a small shack on a cliff. You knock on the door and a frail woman "
                  "opens. She beckons you in and tells you a story of youth and greed. You find this all odd and as "
                  "you try to leave you notice a faint wisper. Before you can even consider what it may be your face "
                  "hits the floor. You are now the women's. You cannot escape.")
    else:
        print("You denied the figure, it becomes angry and lunges at you. You fall into the cold water and drown.")
else:
    print("You went into the forest and got lost. You died of exhaustion.")
