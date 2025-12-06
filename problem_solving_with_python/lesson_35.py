from pathlib import Path  # Import Path module

path = Path()  # Current directory path

# Loop through all .py files
for file in path.glob('*.py'):
    print(file)  # Print file path