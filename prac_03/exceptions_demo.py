"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
when entering other than numbers and decimals.
2. When will a ZeroDivisionError occur?
When the denominator is zero.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?

"""

valid_input = False

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while not valid_input:
        if denominator != 0:
            valid_input = True
        else:
            print("Cannot divide by zero!")
            denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
