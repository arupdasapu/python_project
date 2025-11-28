# Function to calculate total cost
def total_cost(price, shipping, discount):
    print(f"Total cost: ${price + shipping - discount}")

# Call the total_cost function with keyword arguments
total_cost(shipping=5, discount=1, price=10)

# Function to greet the user by first and last name
def welcome(fist_name, middle_name,last_name):
    print(f"Hi {fist_name} {middle_name} {last_name}")

# Call the welcome function with arguments
welcome("Arup", "Das", "Apu") #welcome function used in Prints a greeting using first, middle, and last name

