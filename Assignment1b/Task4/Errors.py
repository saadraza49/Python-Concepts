# Errors
try:
    x = int(input("Enter a number: "))
    print(x)
except ValueError:
    print("Invalid input")
except:
    print("Something went wrong")
    