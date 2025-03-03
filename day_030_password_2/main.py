# Exceptions
# try: something to do
# except: do when expection arises
# else: do this if there were no expections
# finally: No matter what run

try:
    file = open("a_file.txt")
except:
    file = open("a_file.txt", "w")
