with open("file1.txt", "r") as file1:
    numbers1 = file1.readlines()

with open("file2.txt", "r") as file2:
    numbers2 = file2.readlines()

result = [n for n.strip() in numbers1 if n in numbers2]

print(result)
