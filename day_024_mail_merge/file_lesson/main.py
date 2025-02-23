# Gave error, reading https://docs.python.org/3/library/functions.html#open
# Solution https://stackoverflow.com/questions/22282760/filenotfounderror-errno-2-no-such-file-or-directory (Windows vs Linux issue)
# used \\ because the frist \ escapes the character.

file = open("..\\100 Days of Code\\day_024_mail_merge\\file_lesson\\my_file.txt")
contents = file.read()
print(contents)
