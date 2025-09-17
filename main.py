# main.py - Secure Password Strength Analyzer

import re

def check_length(password):
    """
    Analyzes the password length and returns a score component (0–30).
    Longer passwords get more points.
    """
    length = len(password)
    if length < 6:
        return 0
    elif 6 <= length < 10:
        return 10
    elif 10 <= length < 14:
        return 20
    else:
        return 30


def check_character_variety(password):
    """
    Analyzes presence of uppercase, lowercase, digits, and special characters.
    Returns a score component (0–30).
    """
    score = 0
    if re.search(r"[a-z]", password):
        score += 10
    if re.search(r"[A-Z]", password):
        score += 10
    if re.search(r"\d", password):
        score += 5
    if re.search(r"[^A-Za-z0-9]", password):
        score += 5
    return score


def check_commonality(password, common_passwords_list):
    """
    Checks if the password is in the list of common passwords.
    If found, return penalty (-50).
    """
    return -50 if password.lower() in common_passwords_list else 0


def calculate_final_score(password, common_passwords_list):
    """
    Calls all check functions and calculates a final strength score (0–100).
    Returns a tuple (score, rating, feedback).
    """
    base_score = 0
    base_score += check_length(password)
    base_score += check_character_variety(password)
    base_score += check_commonality(password, common_passwords_list)

    # Normalize score between 0–100
    final_score = max(0, min(100, base_score))

    # Qualitative rating
    if final_score < 30:
        rating = "Very Weak"
        feedback = "Too short or too simple. Use longer passwords with mixed characters."
    elif 30 <= final_score < 60:
        rating = "Weak"
        feedback = "Consider adding uppercase letters, numbers, and symbols."
    elif 60 <= final_score < 80:
        rating = "Moderate"
        feedback = "Good start, but increase length or complexity for stronger protection."
    elif 80 <= final_score < 100:
        rating = "Strong"
        feedback = "Solid password! For maximum safety, avoid reusing it elsewhere."
    else:  # 100
        rating = "Very Strong"
        feedback = "Excellent password! Long, complex, and uncommon."

    print(f"\nPassword Analysis Report")
    print(f"------------------------")
    print(f"Score: {final_score}/100")
    print(f"Strength: {rating}")
    print(f"Feedback: {feedback}")

def load_passwords(filename="10k-most-common.txt"):
    """Loads a list of common passwords from a text file."""
    try:
        with open(filename, "r") as f:
            passwords = [line.strip().lower() for line in f]
        return passwords
    except FileNotFoundError:
        print(f"Error: The password list file '{filename}' was not found. The commonality check will be skipped.")
        return []
    
def main():
    """The main function to run the password analyzer tool."""
    common_passwords = load_passwords()
    if not common_passwords:
        # If the list couldn't be loaded, we can't proceed effectively.
        return

    user_password = input("Enter the password to analyze: ")
    calculate_final_score(user_password, common_passwords)

if __name__ == "__main__":
    main()
