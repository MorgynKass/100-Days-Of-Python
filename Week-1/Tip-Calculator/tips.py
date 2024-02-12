# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇
print("Welcome to the tip calculator!")
bill = input("What was the total bill?\n")
tip = input("What percentage of tip do you want to give?\n")
people = input("How many people are splitting the bill?\n")

bill_int = int(bill)
# print(bill_int)

tip_percent = int(tip) / 100
# print(tip_percent)
new_tip = tip_percent + 1

people_int = int(people)

total = round((bill_int / people_int) * new_tip, 2)
# print(total)

print(f"Each person should pay: ${total}")
