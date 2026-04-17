# ============================================================
#   HUNARMAND PUNJAB – Python Programming Master Class
#   Course    : Python Programming – Master Class
#   Instructor: Akbar Ali
# ============================================================

# ============================================================
# PART 1 – Python Basics & Input/Output  [5 Marks]
# ============================================================
print("=" * 60)
print("PART 1 – Python Basics & Input/Output")
print("=" * 60)

# Print messages
print("Welcome to Hunarmand Punjab – Python Master Class!")
print("Instructor: Akbar Ali")

# Simulated input (using variables so script runs non-interactively)
# In real use: name = input("Enter your name: ")
name = "Ahmad"
print(f"\nHello, {name}! Let's start Python.")

# Basic arithmetic
a, b = 18, 5
print(f"\nBasic Arithmetic  (a={a}, b={b}):")
print(f"  Addition       : {a} + {b} = {a + b}")
print(f"  Subtraction    : {a} - {b} = {a - b}")
print(f"  Multiplication : {a} * {b} = {a * b}")
print(f"  Division       : {a} / {b} = {a / b:.2f}")
print(f"  Floor Division : {a} // {b} = {a // b}")
print(f"  Modulus        : {a} % {b} = {a % b}")

# Simple Calculator function
def calculator(x, y, op):
    if   op == '+': return x + y
    elif op == '-': return x - y
    elif op == '*': return x * y
    elif op == '/':
        if y == 0:
            return "Error: Division by zero!"
        return x / y
    else:
        return "Unknown operator"

print("\nSimple Calculator Demo:")
for op in ['+', '-', '*', '/']:
    print(f"  {a} {op} {b} = {calculator(a, b, op)}")
