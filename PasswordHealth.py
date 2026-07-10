import re
# string for special characters
special_characters = "!@#$%^&*"

# Get users password and 
password = input(len("What is you password"))

# Check for length (len)
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


# run the program
if __name__ == "__main__":
    pass