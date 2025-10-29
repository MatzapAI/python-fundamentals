print("---STUDENT GRADES---")

grades = [8.5, 7.0, 9.3, 6.8, 10.0, 8.7, 9.0]

print(f"first three notes: {grades[:3]}")
print(f"three last notes: {grades[-3:]}")
print(f"peer exams: {grades[1::2]}")
invert = grades[::-1]
last_three = invert[-3:]
print(f"inverted list: {invert}")
print(f"the average of the last three inverted: {sum(last_three) / len(last_three):.2f}")



