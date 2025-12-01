# Define a class for Laptop
class Laptop:
    # Method to print parts of the laptop
    def parts(self):
        print('Keyboard, Display, Motherboard')

# Create an instance of Laptop and call the parts method
my_laptop = Laptop()
my_laptop.parts()

# Define a class Desktop that inherits from Laptop
class Desktop(Laptop):
    # Method to print weight of desktop
    def weight(self):
        print('Desktops are heavy-weight')

# Create an instance of Desktop, and call both parts and weight methods
my_desktop = Desktop()
my_desktop.parts()  # Inherited from Laptop
my_desktop.weight()  # Defined in Desktop
