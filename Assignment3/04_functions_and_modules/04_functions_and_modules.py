# ============================================================
# PART 4 – Functions & Modules  [5 Marks]
# ============================================================
print("=" * 60)
print("PART 4 – Functions & Modules")
print("=" * 60)

# Reusable function with parameters & return
def rectangle_area(length, width):
    """Returns area of a rectangle."""
    return length * width

def circle_area(radius):
    import math
    return round(math.pi * radius ** 2, 2)

print(f"rectangle_area(8, 5)  = {rectangle_area(8, 5)}")
print(f"circle_area(7)        = {circle_area(7)}")

# Default arguments
def power(base, exp=2):
    return base ** exp

print(f"\npower(4)     = {power(4)}   (default exp=2)")
print(f"power(4, 3)  = {power(4, 3)}")

# *args
def total(*args):
    return sum(args)

print(f"\ntotal(10, 20, 30, 40) = {total(10, 20, 30, 40)}")

# **kwargs
def display_profile(**kwargs):
    print("  User Profile:")
    for k, v in kwargs.items():
        print(f"    {k}: {v}")

print()
display_profile(name="Zara", age=22, city="Lahore", course="Python")

# MyModule simulation (inline)
print("\nMyModule (inline simulation):")

def my_greet(name):
    return f"Hello, {name}! Welcome to Python Master Class."

def my_square(n):
    return n * n

def my_is_even(n):
    return n % 2 == 0

print(f"  my_greet('Usman')  → {my_greet('Usman')}")
print(f"  my_square(9)       → {my_square(9)}")
print(f"  my_is_even(14)     → {my_is_even(14)}")

# Standard modules
import math, random
print(f"\nmath.log(100, 10)  = {math.log(100, 10)}")
print(f"math.gcd(48, 18)   = {math.gcd(48, 18)}")
print(f"random.uniform(1,10) = {random.uniform(1, 10):.4f}")
