# Check positive, negative, or zero
def check_number(num):  
    if num > 0:
        print(f"  {num} is Positive")
    elif num < 0:
        print(f"  {num} is Negative")
    else:
        print(f"  {num} is Zero")

print("Number Check:")
for val in [7, -3, 0]:
    check_number(val)

# Simple grading system
def grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

print("\nGrading System:")
for m in [95, 82, 74, 63, 55, 40]:
    print(f"  Marks {m:3d} → Grade {grade(m)}")
