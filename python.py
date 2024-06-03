import random
import string
import re

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special):
    if length < 4:
        raise ValueError("Password length must be at least 4 characters")

    character_sets = []
    if use_uppercase:
        character_sets.append(string.ascii_uppercase)
    if use_lowercase:
        character_sets.append(string.ascii_lowercase)
    if use_numbers:
        character_sets.append(string.digits)
    if use_special:
        character_sets.append(string.punctuation)

    if not character_sets:
        raise ValueError("At least one character set must be selected")

    # Ensure at least one character from each selected set is in the password
    password = [random.choice(char_set) for char_set in character_sets]
    
    # Fill the rest of the password length with random choices from the combined sets
    all_characters = ''.join(character_sets)
    password += [random.choice(all_characters) for _ in range(length - len(password))]
    
    # Shuffle the password list to avoid predictable patterns
    random.shuffle(password)
    
    return ''.join(password)

def evaluate_strength(password):
    length = len(password)
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    has_digit = re.search(r'\d', password)
    has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

    strength = "Weak"
    if length >= 8 and has_upper and has_lower and has_digit and has_special:
        strength = "Strong"
    elif length >= 6 and ((has_upper and has_lower) or (has_digit and has_special)):
        strength = "Moderate"

    return strength

def main():
    print("Welcome to the Enhanced Password Generator!")
    try:
        length = int(input("Enter the desired length of the password (min 4): "))
    except ValueError:
        print("Please enter a valid number.")
        return

    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    try:
        password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special)
        strength = evaluate_strength(password)
        print(f"Generated Password: {password}")
        print(f"Password Strength: {strength}")

        save = input("Do you want to save the password to a file? (y/n): ").lower() == 'y'
        if save:
            description = input("Enter a description for the password: ")
            with open("saved_passwords.txt", "a") as file:
                file.write(f"{description}: {password}\n")
            print("Password saved to saved_passwords.txt")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
