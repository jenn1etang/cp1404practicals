"""
Email
Estimate: 30minutes
Actual:
"""


def main():
    user_data = {}

    user_email = str(input("Email: "))

    while user_email != "":
        name = extract_name(user_email)
        user_data[name] = user_email
        user_email = str(input("Email: "))


def extract_name(user_email):
    name = user_email.split("@")[0]
    name = name.split(".")
    name = [word.title() for word in name]
    name = " ".join(name)
    return name


main()
