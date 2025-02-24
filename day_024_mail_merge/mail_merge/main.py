# TODO: Create a letter using starting_letter.txt
with open("./Input/Letters/starting_letter.txt", "r") as letter:
    pass
# for each name in invited_names.txt
with open("./Input/Names/invited_names.txt", "r") as invite:
    names = invite.readlines()
# Replace the [name] placeholder with the actual name.
with open("./Input/Letters/starting_letter.txt", "w") as letter:
    letter_contents = letter.read()
    for name in names:
        new_letter = letter_contents.replace("[name]", name)

# Save the letters in the folder "ReadyToSend".
with open("./Output/ReadyToSend/", "w") as letter:
    pass

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
