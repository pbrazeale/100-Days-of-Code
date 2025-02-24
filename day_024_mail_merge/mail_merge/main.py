# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
with open("day_024_mail_merge\\mail_merge\\Input\\Names\\invited_names.txt") as invites:
    names = invites.readlines()
# Replace the [name] placeholder with the actual name.
with open(
    "day_024_mail_merge\\mail_merge\\Input\\Letters\\starting_letter.txt"
) as letter:
    letter_contents = letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace("[name]", stripped_name)
        # Save the letters in the folder "ReadyToSend".
        with open(
            f"day_024_mail_merge\\mail_merge\\Output\\ReadyToSend\\letter_for_{stripped_name}.txt",
            "w",
        ) as formatted_letter:
            formatted_letter.write(new_letter)

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
