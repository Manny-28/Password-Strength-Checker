import string

#The scoring system for password strength
def check_password(password, common_list):
    """Evaluate a password and return (score, feedback_list)."""
    score = 0
    feedback = []

    # Length checks
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters.")

    if len(password) >= 12:
        score += 1

    # Character variety checks
    if any(c in string.ascii_uppercase for c in password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if any(c in string.digits for c in password):
        score += 1
    else:
        feedback.append("Add at least one digit.")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("Add at least one special character (e.g., !, @, #).")

    # Common password check (overrides all other scoring)
    if password.lower() in common_list:
        score = 0
        feedback = ["This password is in the common-passwords list. Choose another."]

    return score, feedback

def main(): # Main function to run the password checker
    strength_labels = {
        0: "Weak", 1: "Weak",
        2: "Moderate", 3: "Moderate",
        4: "Strong", 5: "Strong"
    }


    while True: #user input loop
        password = input("\nEnter a password to check (or 'quit' to exit): ")

        if password.lower() == "quit":
            print("Goodbye.")
            break

        if len(password) == 0:
            print("Password cannot be empty. Try again.")
            continue

        score, feedback = check_password(password, common_list)
        label = strength_labels.get(score, "Unknown")

        print(f"\nStrength: {label} ({score}/5)")

        if feedback:
            print("Suggestions:")
            for tip in feedback:
                print(f"  - {tip}")

        # Log the result (mask the actual password with asterisks)
        with open("password_log.txt", "a") as log:
            log.write(f"Password: {'*' * len(password)} | Strength: {label} ({score}/5)\n")

main()
