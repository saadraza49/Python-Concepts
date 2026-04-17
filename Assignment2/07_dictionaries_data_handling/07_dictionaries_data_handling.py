# Making a simple dictionary
student = {"name": "Fatima", "age": 19, "grade": "A"}
print(f"Student dict: {student}")

# Access values
print(f"\nName: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

# Update values
student["age"] = 20
student["grade"] = "A+"
print(f"Updated → {student}")

# Loop through items
print("\nKey-Value pairs:")
for key, value in student.items():
    print(f"  {key}: {value}")

# Nested dictionary
class_students = {
    "S001": {"name": "Ali",   "marks": 88},
    "S002": {"name": "Sara",  "marks": 92},
    "S003": {"name": "Umar",  "marks": 76},
}
print("\nClass Students:")
for sid, info in class_students.items():
    print(f"  {sid} → {info['name']}: {info['marks']}")
