"""
CP1404 - Guitar class
Estimate time: 1hour
Actual time: 36mins
"""
from operator import attrgetter


class Guitar:
    """Represent information about a guitar"""

    def __init__(self, name, year, cost):
        """Construct a Guitar from given value"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string presentation of a Guitar"""
        return f"{self.name}, {self.year}, ${self.cost:.2f}"

    def __lt__(self, other):
        return self.year < other.year


def run_tests():
    guitars = []
    in_file = open('guitars.csv', 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    # Close the file as soon as we've finished reading it
    in_file.close()
    guitars.sort()
    for guitar in guitars:
        print(guitar)


if __name__ == "__main__":
    run_tests()
