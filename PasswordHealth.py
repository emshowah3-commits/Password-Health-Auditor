import re
# string for special characters
special_characters = "!@#$%^&*"

# Get users password and 
password = input("What is you password")

# Check for length (len)
password_length = len(password)
# len().password

# check for uppercase letters
has_upper = any(len(char.isupper() for char in password))
# check for numbers
def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# check for special characters
def has_special_char(password): # \s clears for white spaces
    pattern = r'[^a-zA-Z0-9\s]'
    return bool(re.search(pattern, password))

# Print the final report
# Checks for password length
print("Password length check")
if password >= 16:
    print("Password length good")
elif password == 16:
    print("decent")
else:
    print("not so well password length")

# Password uppercase check
print("password uppercase check")
if has_upper >= 15:
    print("Amount of uppercase letters are good")
elif has_upper == 15:
    print("decent")
else:
    print("password uppercase not so well")
# Feedback on collected errors (if/ else statments)

# run the program
if __name__ == "__main__":
    pass