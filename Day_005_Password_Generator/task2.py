student_scores = [125, 98, 214, 135, 100, 98, 97, 23, 54]

print(max(student_scores))

max = student_scores[0]
for score in student_scores:
    if score > max:
        max = score

print(max)