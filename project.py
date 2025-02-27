import random
import re

def generate_password(length=8):

    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    special_characters = "!@#$%^&*()-_=+[]{}|;:,.<>?/~"

    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    password = ""
    for _ in range(length):
        password += random.choice(all_characters)

    return password

def is_strong_password(password):
    return bool(re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%?&])[A-Za-z\d@$!%?&]{8,}$', password))

def get_valid_password():
    while True:
        password = input("Enter a password (at least 8 characters containing at least one lowercase letter, one uppercase letter, one digit, and one special character): ")
        if is_strong_password(password):
            return password
        else:
            print("Password is not strong enough. Please try again.")

def main():
    print("Welcome to the Secure Password Generator!")

    length = int(input("Enter the length of the password you want to generate (default is 12 ): "))
    if length < 8:
        print("Password length must be at least 8. Defaulting to length 12.")
        length = 12

    password = generate_password(length)
    print("Generated Password:", password)

    print("\nLet's check if the generated password is strong:")
    if is_strong_password(password):
        print("The generated password is strong!")
    else:
        print("The generated password is weak. Please consider generating a new one.")

    print("\nNow, let's prompt the user to enter a valid password:")
    valid_password = get_valid_password()
    print("Valid Password:", valid_password)

if __name__ == "__main__":
    main()
