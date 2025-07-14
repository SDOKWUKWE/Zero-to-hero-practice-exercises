'''Write a Python program to check the validity of passwords input by users.
Validation :
At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.
'''


alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


upper_case=[item.upper() for item in alphabet]
num=['0','1','2','3','4','5','6','7','8','9']
character=['$','#','@']

password= input("password: ")
password==alphabet==upper_case==num==character
for pasw in password:
    if len(password) < 6 and len(password) > 16:
        print("correct")



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
'''