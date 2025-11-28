# Define a class for Keyboard with constructor for language and connection type
class Keyboard:
    # Constructor to initialize language and connection
    def __init__(self, language, connection):
        self.language = language
        self.connection = connection

    # Method to print definition of keyboard
    def definition(self):
        print("Keyboard is an input device")

    # Method to print number of keys on keyboard
    def numer_of_keys(self):
        print("There are 101 keys")

# Create an instance of Keyboard with language and connection type
my_keyboard = Keyboard('English', 'wireless')
print(my_keyboard.connection)  # Print connection type

# Define a class AboutMe with constructor for personal details
class AboutMe:
    # Constructor to initialize personal information
    def __init__(self, name, address, occupation):
        self.name = name
        self.address = address
        self.occupation = occupation

    # Method to print personal introduction
    def talk(self):
        print(f"My name is {self.name}. I am from {self.address}. And "
              f"I am a {self.occupation}")

# Create instances of AboutMe and call the talk method
faruqui = AboutMe('Arup Das Apu', 'Bangladesh', 'Data Engineer')
faruqui.talk()

russel = AboutMe('David Russel', 'UK', 'Web Developer')
russel.talk()
