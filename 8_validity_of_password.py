'''Write a Python program to check the validity of passwords input by users.
Validation :
At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 character
'''

import re

def is_valid_password(password):
    # Check length
    if len(password) < 6 or len(password) > 16:
        return False
    # Check for lowercase letter
    if not re.search(r'[a-z]', password):
        return False
    # Check for uppercase letter
    if not re.search(r'[A-Z]', password):
        return False
    # Check for digit
    if not re.search(r'[0-9]', password):
        return False
    # Check for special character
    if not re.search(r'[$#@]', password):
        return False
    return True

if __name__ == "__main__":
    password = input("Enter password: ")
    if is_valid_password(password):
        print("Valid password")
    else:
        print("Invalid password")
