import random  # Import random module

# Generate 5 random numbers between 5 and 10
for i in range(5):
    print(random.randint(5, 10))

# Select a random member from the list
member_list = ['A', 'B', 'C', 'D', 'E']
member = random.choice(member_list)