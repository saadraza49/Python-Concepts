# Add two numbers
def add(a, b):
    return a + b

print(f"add(8, 12) = {add(8, 12)}")

# Check prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

print("\nPrime check:")
for n in [2, 7, 10, 13, 25, 29]:
    print(f"  {n} → {'Prime' if is_prime(n) else 'Not Prime'}")

# Default arguments
def greet(name, msg="Welcome to Hunarmand Punjab!"):
    print(f"  Hello {name}, {msg}")

print("\nDefault argument:")
greet("Ahmad")
greet("Sara", "Keep learning!")

# *args
def sum_all(*args):
    return sum(args)

print(f"\n*args  sum_all(1,2,3,4,5) = {sum_all(1, 2, 3, 4, 5)}")

# **kwargs
def student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print("\n**kwargs student_info:")
student_info(name="Usman", age=21, city="Lahore")
