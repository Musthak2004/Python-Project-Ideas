# Calculator
# Using functions
def add(num1, num2): # add
    return num1 + num2

def subtract(num1, num2): # subtract
    return num1 - num2

def multiply(num1, num2): # multiply
    return num1 * num2

def divide(num1, num2): # divide
    return num1 / num2

# Using loop
while True:
    print("\n--- Simple Calculator ---")
    print('1. Add')
    print('2. Subtract')
    print('3. Multiply')
    print('4. Divide')
    print('5. Exit')

    action = int(input('\nEnter your action (1-5) >>> '))

    if action == 5:
        print('Exiting..... Goodbye!')
        break

    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))

    if action == 1:
        print(f'\nAddition: {add(num1, num2)}')

    elif action == 2:
        print(f'\nSubtraction: {subtract(num1, num2)}')

    elif action == 3:
        print(f'\nMultiplication: {multiply(num1, num2)}')

    elif action == 4:
        if num2 == 0:
            print('\nError: cannot divide by zero.')
        else:
            print(f'\nDivision: {divide(num1, num2)}')

    else:
        print('\nInvalid action.! Please try again later')