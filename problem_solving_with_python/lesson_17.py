# 2D list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Print the whole matrix
print(matrix)

# Access and print element at first row, third column
print(matrix[0][2])

# Update element at first row, third column to 15
matrix[0][2] = 15

# Print updated matrix
print(matrix)

# Loop through each row and item
for row in matrix:
    for item in row:
        print(item)