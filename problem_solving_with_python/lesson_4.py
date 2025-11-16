# Ask user to enter temperature in Celsius

celsius = input('Temperature in Celsius : ')

# Convert the input from text to number (integer)
celsius = int(celsius)

# Calculate temperature in Fahrenheit
fahrenheit = (celsius * (9/5)) + 32

# Print the Fahrenheit value
print(fahrenheit, 'F')