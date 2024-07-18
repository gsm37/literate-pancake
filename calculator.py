logo = '''
 _____________________
|  _________________  |
| |              0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | ÷ | |
| |___|___|___| |___| |
|_____________________|
'''
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide
              }
def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for operation in operations:
        print(operation)

    run = True
    while run:

        op_symbol = input("Pick an operation from the line above: ")

        num2 = float(input("What's the second number?: "))

        calc_function = operations[op_symbol]
        answer = calc_function(num1,num2)

        print(f"{num1} {op_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with the {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            run = False
            calculator()

calculator()