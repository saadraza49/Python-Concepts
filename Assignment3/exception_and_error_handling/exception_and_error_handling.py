# ============================================================
# PART 6 – Exception & Error Handling  [5 Marks]
# ============================================================
print("=" * 60)
print("PART 6 – Exception & Error Handling")
print("=" * 60)

ERROR_LOG = "error_log.txt"

def log_error(error_msg):
    """Log error to file."""
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(ERROR_LOG, "a") as f:
        f.write(f"[{timestamp}] ERROR: {error_msg}\n")

# Basic try/except
print("1. Division by zero:")
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"  Caught ZeroDivisionError: {e}")
    log_error(str(e))

# Multiple exceptions
print("\n2. Multiple Exception Handling:")
test_cases = ["50", "0", "abc", None]
for val in test_cases:
    try:
        num = int(val)
        res = 200 / num
        print(f"  200 / {num} = {res}")
    except ZeroDivisionError as e:
        msg = f"ZeroDivisionError with val='{val}': {e}"
        print(f"  {msg}")
        log_error(msg)
    except (ValueError, TypeError) as e:
        msg = f"ValueError/TypeError with val='{val}': {e}"
        print(f"  {msg}")
        log_error(msg)

# File not found
print("\n3. FileNotFoundError:")
try:
    with open("nonexistent_file.txt", "r") as f:
        data = f.read()
except FileNotFoundError as e:
    print(f"  Caught: {e}")
    log_error(str(e))

# Index error
print("\n4. IndexError:")
try:
    lst = [1, 2, 3]
    print(lst[10])
except IndexError as e:
    print(f"  Caught: {e}")
    log_error(str(e))

# else & finally
print("\n5. try / except / else / finally:")
try:
    x = int("99")
except ValueError as e:
    print(f"  Error: {e}")
else:
    print(f"  Success! Converted to int: {x}")
finally:
    print("  'finally' block always runs.")

print(f"\nAll errors logged to '{ERROR_LOG}'")
print("Error Log Contents:")
with open(ERROR_LOG, "r") as f:
    print(f.read())
