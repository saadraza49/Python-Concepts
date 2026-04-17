import math
import random

print(f"math.sqrt(144)       = {math.sqrt(144)}")
print(f"math.sqrt(2)         = {math.sqrt(2):.6f}")
print(f"math.factorial(7)    = {math.factorial(7)}")
print(f"math.pi              = {math.pi:.6f}")
print(f"math.ceil(4.3)       = {math.ceil(4.3)}")
print(f"math.floor(4.9)      = {math.floor(4.9)}")

print(f"\nrandom.randint(1,100)  = {random.randint(1, 100)}")
print(f"random.randint(1,100)  = {random.randint(1, 100)}")
print(f"random.choice([1,2,3]) = {random.choice([1, 2, 3])}")

rand_list = list(range(1, 11))
random.shuffle(rand_list)
print(f"random.shuffle(1-10)   = {rand_list}")
