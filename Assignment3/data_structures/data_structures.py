# ============================================================
# PART 3 – Data Structures  [5 Marks]
# ============================================================
print("=" * 60)
print("PART 3 – Data Structures")
print("=" * 60)

# --- LIST ---
print("LIST:")
subjects = ["Math", "Science", "English", "Urdu", "Computer"]
print(f"  Original  : {subjects}")
subjects.append("Physics")
print(f"  After append: {subjects}")
subjects.remove("Urdu")
print(f"  After remove 'Urdu': {subjects}")
subjects[0] = "Advanced Math"
print(f"  After update index 0: {subjects}")
print(f"  Length: {len(subjects)}")

# --- TUPLE ---
print("\nTUPLE:")
dimensions = (1920, 1080, 32)
print(f"  Dimensions: {dimensions}  (immutable)")
print(f"  Width={dimensions[0]}, Height={dimensions[1]}, Depth={dimensions[2]}")

# --- SET ---
print("\nSET:")
s1 = {10, 20, 30, 40, 50}
s2 = {30, 40, 50, 60, 70}
print(f"  Set1: {s1}")
print(f"  Set2: {s2}")
print(f"  Union       : {s1 | s2}")
print(f"  Intersection: {s1 & s2}")
print(f"  Difference  : {s1 - s2}")

# --- DICTIONARY – Student Mark System ---
print("\nDICTIONARY – Student Mark System:")
students_marks = {
    "Ali":    {"Math": 88, "Science": 92, "English": 79},
    "Sara":   {"Math": 95, "Science": 87, "English": 91},
    "Bilal":  {"Math": 72, "Science": 68, "English": 75},
}

def get_grade(avg):
    if avg >= 90: return "A+"
    elif avg >= 80: return "A"
    elif avg >= 70: return "B"
    elif avg >= 60: return "C"
    else: return "F"

print(f"  {'Name':<10} {'Math':<8} {'Science':<10} {'English':<10} {'Avg':<8} {'Grade'}")
print("  " + "-" * 52)
for name, marks in students_marks.items():
    avg = sum(marks.values()) / len(marks)
    print(f"  {name:<10} {marks['Math']:<8} {marks['Science']:<10} {marks['English']:<10} {avg:<8.1f} {get_grade(avg)}")

# CRUD on dictionary
print("\nCRUD Operations:")
students_marks["Hina"] = {"Math": 85, "Science": 90, "English": 88}  # Create
print(f"  Create: Added Hina → {students_marks['Hina']}")
print(f"  Read  : Ali's Math = {students_marks['Ali']['Math']}")
students_marks["Ali"]["Math"] = 95                                     # Update
print(f"  Update: Ali's Math → {students_marks['Ali']['Math']}")
del students_marks["Bilal"]                                            # Delete
print(f"  Delete: Removed Bilal. Remaining: {list(students_marks.keys())}")
