import re
# string for special characters
special_characters = "!@#$%^&*"

# Get users password and 
password = input("What is you password: ")

# Check for length (len)
password_length = len(password)
# len().password

# check for uppercase letters
has_upper = len(password) <= 15 and any(char.isupper() for char in password)
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
print("Password length check""\n")

if len(password) >= 16:
    print("Password length good""\n")
elif len(password) == 16:
    print("decent""\n")
else:
    print("not so well password length""\n")

# Password uppercase check
print("password uppercase check""\n")

if has_upper <= 15:
    print("Amount of uppercase letters are good""\n")
elif has_upper == 15:
    print("decent""\n")
else:
    print("password uppercase not so well""\n")
# Feedback on collected errors (if/ else statments)

# run the program
if __name__ == "__main__":
    pass