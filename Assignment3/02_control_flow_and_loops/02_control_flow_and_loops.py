# ============================================================
# PART 2 – Control Flow & Loops  [5 Marks]
# ============================================================
print("=" * 60)
print("PART 2 – Control Flow & Loops")
print("=" * 60)

# if-elif-else
score = 78
print(f"Score = {score}")
if score >= 90:
    print("  Grade: A+ – Excellent!")
elif score >= 80:
    print("  Grade: A – Very Good!")
elif score >= 70:
    print("  Grade: B – Good!")
elif score >= 60:
    print("  Grade: C – Average")
elif score >= 50:
    print("  Grade: D – Below Average")
else:
    print("  Grade: F – Fail")

# for loop
print("\nfor loop – 1 to 10:")
print(" ", end="")
for i in range(1, 11):
    print(i, end="  ")
print()

# while loop
print("\nwhile loop – countdown from 5:")
c = 5
while c > 0:
    print(f"  {c}...")
    c -= 1
print("  Go!")

# break & continue
print("\nbreak – stop when i==6:")
for i in range(1, 11):
    if i == 6:
        break
    print(i, end="  ")
print()

print("continue – skip even numbers:")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i, end="  ")
print()

# Nested loop – multiplication table
print("\nMultiplication Table (1–5 x 1–10):")
for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i*j:4}", end="")
    print()
