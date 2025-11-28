# Try block to handle potential errors
try:
    # Take user input and convert to integer
    celsius = int(input("Temperature in Celsius: "))

    # Convert Celsius to Fahrenheit
    fahrenheit = (celsius * (9/5)) + 32
    print(fahrenheit)

    # Print the F to C ratio (F/C)
    print(f"F to C ratio (F/C): {fahrenheit/celsius}")

# Handle ValueError if the input is not a valid number
except ValueError:
    print('Invalid input')

# Handle ZeroDivisionError if Celsius is 0 (can't divide by 0)
except ZeroDivisionError:
    print('Celsius cannot be 0')