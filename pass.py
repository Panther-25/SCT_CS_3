import re

def check_password_strength(password):
    # Criteria
    length_error = len(password) < 8
    lowercase_error = re.search(r"[a-z]", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    digit_error = re.search(r"[0-9]", password) is None
    special_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Strength calculation
    errors = [length_error, lowercase_error, uppercase_error, digit_error, special_error]
    score = 5 - sum(errors)  # Max score = 5

    # Feedback
    if score == 5:
        strength = "Very Strong ✅"
    elif score == 4:
        strength = "Strong 💪"
    elif score == 3:
        strength = "Moderate 😐"
    elif score == 2:
        strength = "Weak ⚠️"
    else:
        strength = "Very Weak ❌"

    return strength


if __name__ == "__main__":
    password = input("Enter your password: ")
    result = check_password_strength(password)
    print(f"Password Strength: {result}")
