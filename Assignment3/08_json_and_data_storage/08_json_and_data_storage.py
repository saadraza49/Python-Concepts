# ============================================================
# PART 8 – JSON & Data Storage  [5 Marks]
# ============================================================
print("=" * 60)
print("PART 8 – JSON & Data Storage")
print("=" * 60)

import json
import os

STUDENT_JSON = "student.json"

# Write JSON
students_data = [
    {"id": "S001", "name": "Ali",    "age": 20, "grade": "A",  "marks": 88},
    {"id": "S002", "name": "Sara",   "age": 19, "grade": "A+", "marks": 95},
    {"id": "S003", "name": "Umar",   "age": 21, "grade": "B",  "marks": 74},
    {"id": "S004", "name": "Fatima", "age": 18, "grade": "A",  "marks": 90},
]

with open(STUDENT_JSON, "w") as f:
    json.dump(students_data, f, indent=4)
print(f"Written to '{STUDENT_JSON}'")

# Read JSON
print("\nReading JSON:")
with open(STUDENT_JSON, "r") as f:
    loaded = json.load(f)
for s in loaded:
    print(f"  {s['id']} | {s['name']:<8} | Age:{s['age']} | Grade:{s['grade']} | Marks:{s['marks']}")

# Add new student (Create)
new_student = {"id": "S005", "name": "Hassan", "age": 22, "grade": "B+", "marks": 82}
loaded.append(new_student)
with open(STUDENT_JSON, "w") as f:
    json.dump(loaded, f, indent=4)
print(f"\nAdded: {new_student['name']}")

# Update a record
for s in loaded:
    if s["id"] == "S003":
        s["grade"] = "A"
        s["marks"] = 85
with open(STUDENT_JSON, "w") as f:
    json.dump(loaded, f, indent=4)
print("Updated: Umar's grade to A, marks to 85")

# Delete a record
loaded = [s for s in loaded if s["id"] != "S001"]
with open(STUDENT_JSON, "w") as f:
    json.dump(loaded, f, indent=4)
print("Deleted: S001 (Ali)")

# Final state
print("\nFinal JSON state:")
with open(STUDENT_JSON, "r") as f:
    final = json.load(f)
for s in final:
    print(f"  {s['id']} | {s['name']:<8} | Grade:{s['grade']} | Marks:{s['marks']}")
