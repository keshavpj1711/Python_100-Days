# Required Functions
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# Defining operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# Taking input
num1 = float(input("First number: "))

# To print symbols in console
for symbols in operations:
    print(symbols)

while True:
    # To choose operation and call the function accordingly
    operation_choice = input("Pick an operation: ")
    calc_function = operations[operation_choice]

    # Taking input of num2 later for a better user experience
    num2 = float(input("Next number: "))

    # Finding the answer
    answer = calc_function(num1, num2)

    # Finally printing the output
    print(f"{num1} {operation_choice} {num2} = {round(answer, 2)}")

    continuation_choice = input("Type 'y' for calc with {answer} as num1"
                                "Type 'n' to exit: ")
    if continuation_choice == 'y':
        num1 = answer
    else:
        break
