import os

SMS_FILE = "student_management.txt"


# ---------- OOP: Student class ----------
class StudentRecord:
    def __init__(self, name, age, grade):
        self.name  = name
        self.age   = age
        self.grade = grade

    def to_file_line(self):
        return f"{self.name},{self.age},{self.grade}\n"

    def __str__(self):
        return f"Name: {self.name:<15} Age: {self.age:<5} Grade: {self.grade}"


# ---------- Helper functions ----------
def load_students():
    students = []
    if os.path.exists(SMS_FILE):
        with open(SMS_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split(",")
                    if len(parts) == 3:
                        students.append(StudentRecord(parts[0], parts[1], parts[2]))
    return students


def save_students(students):
    with open(SMS_FILE, "w") as f:
        for s in students:
            f.write(s.to_file_line())


def add_student(name, age, grade):
    students = load_students()
    students.append(StudentRecord(name, str(age), grade))
    save_students(students)
    print(f"  ✔ Student '{name}' added successfully.")


def view_students():
    students = load_students()
    if not students:
        print("  No students found.")
        return
    print(f"  {'#':<4} {'Name':<15} {'Age':<6} {'Grade'}")
    print("  " + "-" * 35)
    for i, s in enumerate(students, 1):
        print(f"  {i:<4} {s}")


def update_student(name, new_age=None, new_grade=None):
    students = load_students()
    found = False
    for s in students:
        if s.name.lower() == name.lower():
            if new_age:   s.age   = str(new_age)
            if new_grade: s.grade = new_grade
            found = True
            print(f"  ✔ Student '{name}' updated.")
            break
    if not found:
        print(f"  ✘ Student '{name}' not found.")
    save_students(students)


def delete_student(name):
    students = load_students()
    new_list = [s for s in students if s.name.lower() != name.lower()]
    if len(new_list) == len(students):
        print(f"  ✘ Student '{name}' not found.")
    else:
        save_students(new_list)
        print(f"  ✔ Student '{name}' deleted.")


# ---------- Demo run (no input() so it runs non-interactively) ----------
print("\n--- Adding Students ---")
add_student("Zara",   17, "A+")
add_student("Kamran", 20, "B")
add_student("Hina",   19, "A")

print("\n--- View All Students ---")
view_students()

print("\n--- Update Kamran's grade to A ---")
update_student("Kamran", new_grade="A")
view_students()

print("\n--- Delete Hina ---")
delete_student("Hina")
view_students()

print("\n--- Try deleting non-existent student ---")
delete_student("Ghost")

print("\n" + "=" * 60)
print("  Assignment Complete! All 12 Parts Done.")
print("  Student: [Your Name]  |  Course: Hunarmand Punjab")
print("=" * 60)
