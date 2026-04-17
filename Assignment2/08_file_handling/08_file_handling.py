FILE_NAME = "students_data.txt"

# Write to file
with open(FILE_NAME, "w") as f:
    f.write("--- Student Records ---\n")
    f.write("Name: Saad, Age: 19, Grade: A\n")
    f.write("Name: Abdullah, Age: 19, Grade: A+\n")
print(f"File '{FILE_NAME}' created and written.")

# Read file
print("\nFile Content:")
with open(FILE_NAME, "r") as f:
    print(f.read())

# Append to file
with open(FILE_NAME, "a") as f:
    f.write("Name: Umar, Age: 21, Grade: B\n")
print("Appended new record.\n")

print("File Content after append:")
with open(FILE_NAME, "r") as f:
    print(f.read())
