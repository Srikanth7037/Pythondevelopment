import random
import string

def generate_password(length=12):
    # Define the characters that can be used in the password
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Randomly choose characters from the available ones
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

# Call the function to generate a password
password_length = int(input("Enter the length of the password: "))
generated_password = generate_password(password_length)

print(f"Your generated password is: {generated_password}")
