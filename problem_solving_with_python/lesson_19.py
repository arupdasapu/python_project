# List with duplicate numbers
number_list = [1, 2, 1, 5, 6, 5, 10]

# Empty list to store unique numbers
unique = []

# Loop through each number
for number in number_list:
    if number not in unique:  # Check if number is not already added
        unique.append(number)  # Add unique number to list

print(unique)