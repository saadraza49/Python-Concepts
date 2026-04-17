# Division by zero
def safe_divide(a, b):
    try:
        result = a / b
        print(f"  {a} / {b} = {result}")
    except ZeroDivisionError:
        print(f"  Error: Cannot divide {a} by zero!")
    finally:
        print("  (division attempted)")

print("Division by Zero:")
safe_divide(10, 2)
safe_divide(10, 0)

# Multiple exceptions
def multi_exception_demo(val):
    try:
        number = int(val)
        result = 100 / number
        my_list = [1, 2, 3]
        print(f"  100 / {number} = {result}  |  list[1] = {my_list[1]}")
    except ValueError:
        print(f"  ValueError: '{val}' cannot be converted to int!")
    except ZeroDivisionError:
        print(f"  ZeroDivisionError: division by zero!")
    except IndexError:
        print(f"  IndexError: list index out of range!")
    except Exception as e:
        print(f"  Unexpected error: {e}")

print("\nMultiple Exception Handling:")
multi_exception_demo("5")
multi_exception_demo("0")
multi_exception_demo("abc")
