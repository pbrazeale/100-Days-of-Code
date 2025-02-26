import pandas

student_dict = {"student": ["Angela", "James", "Lilly"], "score": [56, 76, 98]}

student_data_frame = pandas.DataFrame(student_dict)

# for key, value in student_data_frame.items():
#     print(value)

for index, row in student_data_frame.iterrows():
    print(row.score)
