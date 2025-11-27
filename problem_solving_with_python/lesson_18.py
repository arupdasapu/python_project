# List of numbers
number_list = [1, 2, 5, 1, 10, 14]

number_list.append(20)        # Add 20 at the end
number_list.insert(1, 7)      # Insert 7 at index 1
number_list.remove(2)         # Remove first occurrence of 2
number_list.sort()            # Sort the list
number_list.reverse()         # Reverse the list
print(number_list)

print(12 in number_list)       # Check if 12 is in the list
print(number_list.count(1))    # Count how many times 1 appears
print(number_list.index(10))   # Find index of 10

number_list.pop()              # Remove last item

number_list_2 = number_list.copy()  # Copy the list
number_list_2.clear()               # Clear copied list
print(number_list_2)
