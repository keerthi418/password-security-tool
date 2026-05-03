def load_common_passwords():
    """Load common passwords from file"""
    try:
        with open('common_passwords.txt', 'r', encoding='utf-8', errors='ignore') as f:
            return set(line.strip().lower() for line in f)
    except FileNotFoundError:
        print("Warning: common_passwords.txt not found")
        return set()

def check_against_common(password, common_passwords):
    """Check if password is in common passwords list"""
    if password.lower() in common_passwords:
        return False, "❌ This is a commonly used password!"
    return True, "✓ Not in common passwords database"

def check_password_strength(password):
    """Check the strength of a password"""
    
    score = 0
    feedback = []
    
    # Check length
    if len(password) < 8:
        feedback.append("❌ Password too short (minimum 8 characters)")
    elif len(password) < 12:
        feedback.append("⚠️ Password could be longer (recommended 12+ characters)")
        score += 1
    else:
        feedback.append("✓ Good length")
        score += 2
    
    # Check for uppercase
    if any(c.isupper() for c in password):
        feedback.append("✓ Contains uppercase letters")
        score += 1
    else:
        feedback.append("❌ Missing uppercase letters")
    
    # Check for lowercase
    if any(c.islower() for c in password):
        feedback.append("✓ Contains lowercase letters")
        score += 1
    else:
        feedback.append("❌ Missing lowercase letters")
    
    # Check for numbers
    if any(c.isdigit() for c in password):
        feedback.append("✓ Contains numbers")
        score += 1
    else:
        feedback.append("❌ Missing numbers")
    
    # Check for special characters
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    if any(c in special_chars for c in password):
        feedback.append("✓ Contains special characters")
        score += 2
    else:
        feedback.append("❌ Missing special characters")
    
    # Determine strength
    if score <= 3:
        strength = "WEAK"
    elif score <= 5:
        strength = "MODERATE"
    else:
        strength = "STRONG"
    
    return strength, score, feedback


# Test code (optional)
if __name__ == "__main__":
    common_passwords = load_common_passwords()
    
    test_password = input("Enter a password to check: ")
    strength, score, feedback = check_password_strength(test_password)
    is_unique, common_msg = check_against_common(test_password, common_passwords)
    
    print(f"\nStrength: {strength}")
    print(f"Score: {score}/7")
    print("\nFeedback:")
    for item in feedback:
        print(f"  {item}")
    print(f"  {common_msg}")
