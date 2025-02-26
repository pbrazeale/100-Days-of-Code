numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n+1
#     new_list.append(add_1)

# List comperhension
# new_list = [new_item for item in list]
new_list = [n + 1 for n in numbers]

double_list = [n * 2 for n in range(1, 5)]
print(double_list)
