# Take input from user
message = input("Type your message: ")

# Split the message into words
separate_words = message.split(' ')
print(separate_words)

# Dictionary of emojis
emoji = {
    ":)": "😊",
    ":(": "☹"
}

# Build the output with emojis
output = ""
for word in separate_words:
    output += emoji.get(word, word) + " "  # Replace word if emoji exists
print(output)