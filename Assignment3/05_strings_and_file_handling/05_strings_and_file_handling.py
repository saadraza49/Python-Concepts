# ============================================================
# PART 5 – Strings & File Handling  [5 Marks]
# ============================================================
print("=" * 60)
print("PART 5 – Strings & File Handling")
print("=" * 60)

# String operations
s = "  Hunarmand Punjab Python Master Class  "
print(f"Original : '{s}'")
print(f"strip()  : '{s.strip()}'")
print(f"upper()  : '{s.strip().upper()}'")
print(f"lower()  : '{s.strip().lower()}'")
print(f"len()    : {len(s.strip())}")
print(f"replace  : '{s.strip().replace('Python', 'Advanced Python')}'")
print(f"split()  : {s.strip().split()[:4]}  ...")
print(f"slicing  : '{s.strip()[0:10]}'")

# Concatenation & formatting
first, last = "Akbar", "Ali"
full = first + " " + last
print(f"\nConcatenation: '{full}'")
print(f"f-string     : 'Instructor: {full}'")
print(f"find('Punjab'): index = {s.find('Punjab')}")
print(f"startswith   : {s.strip().startswith('Hunarmand')}")
print(f"count 'a'    : {s.lower().count('a')}")

# File: students.txt
STUDENTS_TXT = "students.txt"
with open(STUDENTS_TXT, "w") as f:
    f.write("Name,Age,Grade\n")
    f.write("Ali,20,A\n")
    f.write("Sara,19,A+\n")
    f.write("Umar,21,B\n")
print(f"\nWritten to '{STUDENTS_TXT}'")

print(f"Reading '{STUDENTS_TXT}':")
with open(STUDENTS_TXT, "r") as f:
    for line in f:
        print(f"  {line.strip()}")

# Formatted User Profile System
DATA_FILE = "data.txt"
profiles = [
    {"name": "Fatima", "email": "fatima@example.com", "age": 22, "city": "Karachi"},
    {"name": "Hassan", "email": "hassan@example.com", "age": 25, "city": "Lahore"},
]

with open(DATA_FILE, "w") as f:
    f.write("=" * 40 + "\n")
    f.write("   FORMATTED USER PROFILES\n")
    f.write("=" * 40 + "\n")
    for p in profiles:
        f.write(f"Name  : {p['name']}\n")
        f.write(f"Email : {p['email']}\n")
        f.write(f"Age   : {p['age']}\n")
        f.write(f"City  : {p['city']}\n")
        f.write("-" * 40 + "\n")

print(f"\nFormatted User Profiles (data.txt):")
with open(DATA_FILE, "r") as f:
    print(f.read())
