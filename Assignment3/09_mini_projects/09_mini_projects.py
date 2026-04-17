# ============================================================
# PART 9 – Mini Projects  [10 Marks]
# ============================================================
print("=" * 60)
print("PART 9 – Mini Projects")
print("=" * 60)

import random, re, hashlib, json, os

# -------------------------------------------------------------------
# MINI PROJECT 1: Number Guessing Game (Non-interactive demo)
# -------------------------------------------------------------------
print("\n--- Mini Project 1: Number Guessing Game ---")
print("(Simulated run – in real use, input() prompts the player)")

def play_guessing_game(secret=None, guesses_list=None):
    """
    secret       : the hidden number (random if None)
    guesses_list : list of guesses to simulate (uses input() if None)
    """
    if secret is None:
        secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    print(f"  Game started! Guess a number between 1 and 100.")
    print(f"  You have {max_attempts} attempts.")

    for i in range(max_attempts):
        if guesses_list:
            guess = guesses_list[i] if i < len(guesses_list) else secret
        else:
            guess = int(input(f"  Attempt {i+1}: Enter your guess: "))

        attempts += 1
        print(f"  Attempt {attempts}: Guessed {guess}", end=" → ")

        if guess < secret:
            print("Too LOW! Go higher.")
        elif guess > secret:
            print("Too HIGH! Go lower.")
        else:
            print(f"CORRECT! 🎉 You guessed it in {attempts} attempt(s)!")
            return

    print(f"  Out of attempts! The number was {secret}.")

# Demo with a fixed secret=42
play_guessing_game(secret=42, guesses_list=[20, 60, 40, 45, 42])


# -------------------------------------------------------------------
# MINI PROJECT 2: Registration System
# -------------------------------------------------------------------
print("\n--- Mini Project 2: Registration System ---")

REG_FILE = "student.json"

def hash_password(pwd):
    return hashlib.sha256(pwd.encode()).hexdigest()

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return bool(re.match(pattern, email))

def validate_password(pwd):
    return len(pwd) >= 8

def load_users():
    if os.path.exists(REG_FILE):
        with open(REG_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_users(users):
    with open(REG_FILE, "w") as f:
        json.dump(users, f, indent=4)

def register_user(name, email, password):
    if not name.strip():
        print("  ✘ Name cannot be empty.")
        return False
    if not validate_email(email):
        print(f"  ✘ Invalid email format: '{email}'")
        return False
    if not validate_password(password):
        print("  ✘ Password must be at least 8 characters.")
        return False

    users = load_users()
    for u in users:
        if isinstance(u, dict) and u.get("email") == email:
            print(f"  ✘ Email '{email}' already registered.")
            return False

    users.append({
        "name": name,
        "email": email,
        "password": hash_password(password)
    })
    save_users(users)
    print(f"  ✔ User '{name}' registered successfully!")
    return True

# Demo registrations
print("Registration Demo:")
register_user("Zara Malik",  "zara@example.com",   "securePass1")
register_user("Kamran Ali",  "kamran@example.com", "myPass123")
register_user("Bad Email",   "not-an-email",       "pass1234")    # invalid email
register_user("Short Pass",  "short@example.com",  "1234")        # short password
register_user("Zara Malik",  "zara@example.com",   "anotherPass") # duplicate


# -------------------------------------------------------------------
# MINI PROJECT 3: Authentication System
# -------------------------------------------------------------------
print("\n--- Mini Project 3: Authentication System ---")

def login(email, password):
    users = load_users()
    hashed = hash_password(password)
    for u in users:
        if isinstance(u, dict) and u.get("email") == email:
            if u.get("password") == hashed:
                print(f"  ✔ Login successful! Welcome, {u['name']}!")
                return True
            else:
                print("  ✘ Incorrect password.")
                return False
    print(f"  ✘ No account found for '{email}'.")
    return False

print("Login Demo:")
login("zara@example.com",   "securePass1")   # correct
login("kamran@example.com", "wrongPass")     # wrong password
login("ghost@example.com",  "somePass123")   # not registered
login("zara@example.com",   "wrongPass")     # wrong password for known user
