"""
To enter appropriate password and display in stars.
"""


# imports
# CONSTANTS

def main():
    password = get_password()
    print("\nYou have create a password.", sep=' ')
    display_asterisks(password)


def display_asterisks(password):
    print(password * '*')


def get_password():
    password = password_length_check("Enter password: ", 10)
    return password


def password_length_check(prompt, minimum_length):
    """Gets the password and check with minimum_length and returns length of password"""
    password = str(input(prompt))
    while len(password) < minimum_length:
        print("Invalid password.")
        password = str(input(prompt))
    return len(password)


main()
