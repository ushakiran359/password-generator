
import random
import string
def generate_password(length):
    letters = string.ascii_letters       # a-z + A-Z
    digits = string.digits               # 0-9
    symbols = string.punctuation         # !@#$%^&*()_+ etc.
    all_characters = letters + digits + symbols
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password
def main():
    print("===== PASSWORD GENERATOR =====")
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Password length must be greater than 0.")
            return
    except ValueError:
        print("Invalid input! Please enter a number.")
        return
    password = generate_password(length)
    print(f"\nGenerated Password: {password}\n")
if __name__ == "__main__":
    main()

