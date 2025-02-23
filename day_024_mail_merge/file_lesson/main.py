# Gave error, reading https://docs.python.org/3/library/functions.html#open
# Solution https://stackoverflow.com/questions/22282760/filenotfounderror-errno-2-no-such-file-or-directory (Windows vs Linux issue)
# used \\ because the frist \ escapes the character.

# Corrected issue by chaging my terminal working dir. -_-

# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

with open("new_file.txt", mode="a") as file:
    file.write("\nNew text.")
