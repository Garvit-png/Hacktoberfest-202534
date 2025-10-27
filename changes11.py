import random
import string

def generate_password(length):
    if length < 4:
        raise ValueError("Password length should be at least 4")

    # Character categories
    lower = random.choice(string.ascii_lowercase)
    upper = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    symbol = random.choice(string.punctuation)

    # Remaining characters
    all_chars = string.ascii_letters + string.digits + string.punctuation
    remaining = ''.join(random.choice(all_chars) for _ in range(length - 4))

    # Combine and shuffle
    password_list = list(lower + upper + digit + symbol + remaining)
    random.shuffle(password_list)

    return ''.join(password_list)

# Taking input
length = int(input("Enter password length: "))
print("Generated Password:", generate_password(length))
