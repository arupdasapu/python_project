# Define a class for Keyboard
class Keyboard:
    # Method to print definition of keyboard
    def definition(self):
        print("Keyboard is an input device")

    # Method to print number of keys on keyboard
    def number_of_keys(self):
        print('There are 101 keys')

# Create an instance of Keyboard
my_keyboard = Keyboard()
my_keyboard.definition()          # Call definition method
my_keyboard.number_of_keys()     # Call number_of_keys method
my_keyboard.brand = "Logitech"   # Add brand attribute to the instance
print(my_keyboard.brand)         # Print brand

# Create another instance of Keyboard
new_keyboard = Keyboard()
new_keyboard.definition()        # Call definition method
new_keyboard.brand = "Dell"      # Add brand attribute to the new instance
print(new_keyboard.brand)        # Print brand
