"""
Determines data in list
"""

numbers = []
describe_data = ['first', 'last', 'smallest', 'largest', 'average of the']

for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)

for count in range(0, len(describe_data)):
    print(f"The {describe_data[count]} number is", end=' ')
    if count == 0:
        print(numbers[0])
    elif count == 1:
        print(numbers[-1])
    elif count == 2:
        print(min(numbers))
    elif count == 3:
        print(max(numbers))
    elif count == 4:
        print(sum(numbers)/len(numbers))
