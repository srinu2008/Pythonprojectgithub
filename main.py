students = [
    {"name": "Alice", "math": 85, "eng": 90, "att": 95},
    {"name": "Bob", "math": 92, "eng": 85, "att": 88},
    {"name": "Charlie", "math": 78, "eng": 82, "att": 92},
    {"name": "Diana", "math": 88, "eng": 91, "att": 96}
]

total_math = 0
low_att_students = []
i = 0
while i < len(students):
    s = students[i]
    total_math += s["math"]  # Arithmetic
    avg_sub = (s["math"] + s["eng"]) / 2  # Division
    if avg_sub >= 90:  # Relational
        print(f"{s['name']}: A Grade (Avg: {avg_sub:.1f})")
    elif avg_sub >= 80:
        print(f"{s['name']}: B Grade (Avg: {avg_sub:.1f})")
    else:
        print(f"{s['name']}: C Grade (Avg: {avg_sub:.1f})")

    if s["att"] < 90:  # Logical condition
        low_att_students.append(s["name"])

    i += 1

avg_math_all = total_math / len(students)
print(f"\nOverall Math Avg: {avg_math_all:.1f}")
print("Low Attendance:", low_att_students or "None")

for student in students:
    if student["att"] > avg_math_all:
        print(f"{student['name']} above avg attendance/performance")
