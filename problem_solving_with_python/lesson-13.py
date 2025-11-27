# Set actual price and guess limits

actual_price = 10
guess_count = 0
guess_limit = 5

# Allow up to 5 guesses
while guess_count < guess_limit:
    guess = int(input("Guess the price: "))  # User input
    guess_count += 1  # Increment guess count
    if guess == actual_price:  # Check if guessed correctly
        print("You've won!")  # Congratulate
        break  # Exit loop
else:
    print("You failed")  # If out of guesses