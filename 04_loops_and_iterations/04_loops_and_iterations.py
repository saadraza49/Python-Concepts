# for loop: 1 to 20
print("Numbers 1–20 (for loop):")
print(" ", end="")
for i in range(1, 21):
    print(i, end="  ")
print()

# while loop: even numbers up to 20
print("\nEven numbers up to 20 (while loop):")
print(" ", end="")
n = 2
while n <= 20:
    print(n, end="  ")
    n += 2
print()

# Nested loop – multiplication table (1–5)
print("\nMultiplication Table (1–5):")
for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i*j:4}", end="")
    print()

# break & continue demo
print("\nbreak  demo – stop at 5:")
for i in range(1, 11):
    if i == 6:
        break
    print(i, end="  ")
print()

print("continue demo – skip multiples of 3:")
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i, end="  ")
print()
