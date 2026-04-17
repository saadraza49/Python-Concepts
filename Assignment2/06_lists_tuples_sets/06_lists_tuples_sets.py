# List
fruits = ["Apple", "Mango", "Banana", "Grapes", "Orange"]
print("Fruits List:")
for i, fruit in enumerate(fruits, 1):
    print(f"  {i}. {fruit}")

fruits.append("Strawberry")
print(f"After append: {fruits}")
fruits.remove("Banana")
print(f"After remove 'Banana': {fruits}")

# Tuple (immutable)
coords = (24.8607, 67.0011)
print(f"\nTuple (coordinates): {coords}")
print(f"  Latitude: {coords[0]}, Longitude: {coords[1]}")
try:
    coords[0] = 0   # This will fail
except TypeError as e:
    print(f"  Immutability proven → TypeError: {e}")

# Set operations
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(f"\nSet A = {set_a}")
print(f"Set B = {set_b}")
print(f"  Union        : {set_a | set_b}")
print(f"  Intersection : {set_a & set_b}")
print(f"  Difference   : {set_a - set_b}")
