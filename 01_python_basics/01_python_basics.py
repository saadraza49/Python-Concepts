# Print Hello Hunarmand Punjab
print("Hello Hunarmand Punjab")

# Variables – string, int, float, boolean
name    = "Muhammad Saad Raza"
age     = 19
gpa     = 3.73
is_enrolled = True

print(f"Name: {name}, Age: {age}, GPA: {gpa}, Enrolled: {is_enrolled}")
print(f"Types -> name:{type(name)}  age:{type(age)}  gpa:{type(gpa)}  enrolled:{type(is_enrolled)}")

# Basic arithmetic operations
a, b = 15, 4
print(f"Addition       : {a} + {b} = {a + b}")
print(f"Subtraction    : {a} - {b} = {a - b}")
print(f"Multiplication : {a} * {b} = {a * b}")
print(f"Division       : {a} / {b} = {a / b}")
print(f"Floor Division : {a} // {b} = {a // b}")
print(f"Modulus        : {a} % {b} = {a % b}")
print(f"Exponentiation : {a} ** {b} = {a ** b}")

# Type casting
print("\nType Casting:")
num_str  = "42"
num_int  = int(num_str)
num_float= float(num_str)
back_str = str(num_int)
print(f"str '42' -> int  : {num_int}  ({type(num_int)})")
print(f"str '42' -> float: {num_float} ({type(num_float)})")
print(f"int  42  -> str  : '{back_str}' ({type(back_str)})")
