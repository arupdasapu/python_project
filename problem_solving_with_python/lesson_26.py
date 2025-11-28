# Function to convert text to emoji
def emoji_converted(message):
    separate_words = message.split(' ')  # Split message into words
    emoji = {  # Dictionary of emojis
        ":)": "😊",
        ":(": "☹"
    }
    output = ""
    for word in separate_words:  # Loop through each word
        output += emoji.get(word, word) + " "  # Add emoji or word to output
    return output  # Return final string with emojis

# Take input message from user
message = input("Type your message: ")
# Call function and store result
result = emoji_converted(message)
# Print the converted message with emojis
print(result)