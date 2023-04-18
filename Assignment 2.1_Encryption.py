# Zemerelin Iris M. Membrere
# BSCPE 1-4
# Assignment 2

# Problem 1 - Encryption

# Get an input from the user
ask_input = input("\033[0;31;48mInput a plaintext: \033[35m")
text_output = ("")

# Check if the input has the variables and change it into corresponding symbols
for i in range(len(ask_input)):
# If there is 'a', change to '*'
    if ask_input[i].lower() == 'a':
        text_output += '*'
# If there is 'e', change to '&'
    elif ask_input[i].lower() == 'e':
        text_output += '&'
# If there is 'i', change to '#'
    elif ask_input[i].lower() == 'i':
        text_output += '#'
# If there is 'o', change to '+'
    elif ask_input[i].lower() == 'o':
        text_output += '+'
# If there is 'u', change to '!'
    elif ask_input[i].lower() == 'u':
        text_output += '!'
    else:
        text_output += ask_input[i]
# Print the encrypted input
print(text_output)