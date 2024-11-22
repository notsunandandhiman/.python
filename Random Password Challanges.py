import random
import string

def generate_password(length=12):
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return ''.join(random.sample(password, len(password)))  # Shuffle the password

# Example usage
if __name__ == "__main__":
    password_length = int(input("Enter the desired password length (minimum 6): "))
    if password_length < 6:
        print("Password length should be at least 6.")
    else:
        print(f"Generated Password: {generate_password(password_length)}")