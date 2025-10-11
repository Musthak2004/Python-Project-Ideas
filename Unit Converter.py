def length():
    print("Length: (meter, kilometer):")

    try:
        value = float(input("Enter Value: "))
    except ValueError:
        print("Invalid number")
        return
    
    convert_from = input('Convert from (meter, kilometer): ').lower()
    convert_to = input('Convert to (meter, kilometer): ').lower()

    if convert_from == 'meter' and convert_to == 'kilometer':
        print(f"Result: {value / 1000} kilometers.")
    elif convert_from == 'kilometer' and convert_to == 'meter':
        print(f"Result: {value * 1000} meters.")
    else:
        print('Invalid...')

def weight():
    print('Weight: (kilogram, gram): ')

    try:
        value = float(input("Enter Value: "))
    except ValueError:
        print("Invalid number")
        return
    
    convert_from = input('Convert from (gram, kilogram): ').lower()
    convert_to = input('Convert to (gram, kilogram): ').lower()

    if convert_from == 'gram' and convert_to == 'kilogram':
        print(f"Result: {value / 1000} kilograms.")
    elif convert_from == 'kilogram' and convert_to == 'gram':
        print(f"Result: {value * 1000} grams.")
    else:
        print('Invalid...')

def temperature():
    print('Temperature: (celsius, fahrenheit): ')

    try:
        value = float(input("Enter Value: "))
    except ValueError:
        print("Invalid number")
        return
    
    convert_from = input('Convert from (celsius, fahrenheit): ').lower()
    convert_to = input('Convert to (celsius, fahrenheit): ').lower()

    if convert_from == 'celsius' and convert_to == 'fahrenheit':
        print(f"Result: {(value * 9/5) + 32} F.")
    elif convert_from == 'fahrenheit' and convert_to == 'celsius':
        print(f"Result: {(value - 32) * 5/9} C.")
    else:
        print('Invalid...')

def time():
    print('Time: (seconds, minutes): ')

    try:
        value = float(input("Enter Value: "))
    except ValueError:
        print("Invalid number")
        return
    
    convert_from = input('Convert from (seconds, minutes): ').lower()
    convert_to = input('Convert to (seconds, minutes): ').lower()

    if convert_from == 'seconds' and convert_to == 'minutes':
        print(f"Result: {value / 60} minutes.")
    elif convert_from == 'minutes' and convert_to == 'seconds':
        print(f"Result: {value * 60} seconds.")
    else:
        print('Invalid...')

while True:
    print('\n--- Unit Converter ---')
    print('1. Length')
    print('2. Weight')
    print('3. Temperature')
    print('4. Time')
    print('5. Exit')

    action = input('Enter your actions (1-5): ')

    if action == '1':
        length()
    elif action == '2':
        weight()
    elif action == '3':
        temperature()
    elif action == '4':
        time()
    elif action == '5':
        print('Thank you for using me... GoodBye!')
        break
    else:
        print('Invalid action... Please try again.!')