# Loop through each character in the string 'Python'
for character in 'Python':
    print(character)

# Loop through each item in the list ['Egg', 'Milk', 'Rice']
for item in ['Egg', 'Milk', 'Rice']:
    print(item)

# Loop through each number in the list [1, 2, 3, 4]
for number in [1, 2, 3, 4]:
    print(number)

# Loop through numbers from 0 to 9
for x in range(10):
    print(x)

# Loop through numbers from 5 to 9
for y in range(5, 10):
    print(y)

# Loop through numbers from 5 to 9 with a step of 2
for z in range(5, 10, 2):
    print(z)

# Calculate total sum of bills
bills = [10, 20, 30]
total = 0
for bill in bills:
    total += bill  # Add each bill to total
print(f"Total bill: ${total}")