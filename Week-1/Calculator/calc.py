from art import logo

print(logo)


# Add
def add(a1, a2):
    return a1 + a2


# Subtract
def subtract(s1, s2):
    return s1 - s2


# Multiply
def multiply(m1, m2):
    return m1 * m2


# Divide
def divide(d1, d2):
    return d1 / d2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    calc_continue = True

    num1 = float(input("What is the first number?\n"))
    for op in operations:
        print(op)

    while calc_continue:
        user_operation = input("Pick an operation.\n")
        num2 = float(input("What is the next number?\n"))

        calculations = operations[user_operation]
        answer = calculations(num1, num2)

        print(f"{num1} {user_operation} {num2} = {answer}")

        go_again = input("Would you like to go again?: y or n\n").lower()
        if go_again == "n":
            new_calc = input("Would you like to start a new calculation?: y or n\n")
            if new_calc == "n":
                print("Goodbye!")
                calc_continue = False
            else:
                print(logo)
                calculator()
        else:
            num1 = answer


calculator()