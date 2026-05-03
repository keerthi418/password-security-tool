import secrets
import string

def generate_password(length=16, use_uppercase=True, use_lowercase=True, 
                     use_digits=True, use_special=True):
    """Generate a secure random password"""
    
    # Build character pool
    chars = ""
    
    if use_lowercase:
        chars += string.ascii_lowercase
    
    if use_uppercase:
        chars += string.ascii_uppercase
    
    if use_digits:
        chars += string.digits
    
    if use_special:
        chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    if not chars:
        return "Error: Must select at least one character type"
    
    # Generate password using secrets module
    password = ''.join(secrets.choice(chars) for _ in range(length))
    
    return password


# Test code (optional)
if __name__ == "__main__":
    print("Generated Password:", generate_password(16))