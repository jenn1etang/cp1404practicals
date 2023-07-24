"""
CP1404 -
Estimate time: 30mins
Actual time: 1hour
"""

from prac_06.guitar import Guitar

guitars = []
is_name_blank = False
print("My guitars!")

name = str(input("Name: "))
year = int(input("Year: "))
cost = float(input("Cost: $"))

while not is_name_blank:
    guitars.append(Guitar(name, year, cost))
    print(f"{name} ({year}) : ${cost:,.2f} added.\n")
    name = str(input("Name: "))
    if name == '' or name == ' ':
        is_name_blank = True
        break
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
print('\n...snip...\nThese are my guitars:')

max_length_name = max(len(guitar.name) for guitar in guitars)
max_length_cost = max(len(f"{guitar.cost:,.2f}") for guitar in guitars)

number = 0
for guitar in guitars:
    number += 1
    print(f"Guitar {number}: {guitar.name:>{max_length_name}} ({guitar.year}), worth $ "
          f"{guitar.cost:>{max_length_cost},.2f}", end = ' ')
    if guitar.is_vintage():
        print("(vintage)")
    else:
        print()
