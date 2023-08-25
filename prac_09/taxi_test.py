"""
CP1404 - Test class taxi
Estimate time: 30mins
Actual time: 20mins
"""

from prac_09.taxi import Taxi

# Create a new object
my_taxi = Taxi('Prius 1', 100)

# Drive 40 km
my_taxi.drive(40)

# Display my_taxi detail and current fare
print(my_taxi)

# Restart the meter and then drive the car 100 km
my_taxi.start_fare()
my_taxi.drive(100)

# Display my_taxi detail and current fare
print(my_taxi)

