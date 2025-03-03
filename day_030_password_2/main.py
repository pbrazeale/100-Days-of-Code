# Exceptions
# try: something to do
# except: do when expection arises
# else: do this if there were no expections
# finally: No matter what run

try:
    file = open("a_file.txt")
    a_dictonary = {"key": "value"}
    print(a_dictonary["key"])

# best practice to catch the exact errors you want to handle, rather than all.
except FileNotFoundError:
    file = open("a_file.txt", "w")

# catch the error as a variable
except KeyError as error_message:
    print(f"The Key {error_message} does not exisit.")

else:
    content = file.read()
    print(content)

finally:
    file.close()
    print("file was closed")
