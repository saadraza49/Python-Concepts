# if else task
name = input("Enter your name: ").lower()
if name == "saad":
    print("Hello Saad")
elif name == "abdullah":
    print("Hello Abdullah")
else:
    print("Hello Unknown")

age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

hobby = input("What is your hobby?: ").lower()
if hobby == "reading":
    print("That is great. I love reading")
elif hobby == "gaming":
    print("That is great. I love gaming")
else:
    print("You have no hobby")

print(f"Hello {name}, you are {age} years old and your hobby is {hobby}")

