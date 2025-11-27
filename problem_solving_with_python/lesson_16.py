# List of grocery items
grocery_list = ['egg', 'rice', 'bread', 'sugar']

# Update second item ('rice' to 'oil')
grocery_list[1] = 'oil'

# Print item from index 1 to 2 (only 'oil')
print(grocery_list[1:2])

# Print the full updated grocery list
print(grocery_list)

# List of prices
price = [5, 10, 15, 1, 3, 7]

# Find the maximum value
max = price[0]  # Assume first value is max
for value in price:
    if value > max:
        max = value  # Update max if bigger value found
print(max)