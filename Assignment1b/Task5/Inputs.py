# Input task type conversion
integer = int(input("Enter an integer: "))
decimal = float(input("Enter a decimal: "))

print("Integer: ", integer)
print("Decimal: ", decimal)

print(int(decimal))
print(str(integer))

print(type(int(decimal)))
print(type(str(integer)))