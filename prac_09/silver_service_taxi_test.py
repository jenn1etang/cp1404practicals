"""
CP1404 - silver service taxi class test

Estimate time: 30mins
Actual time: 45mins
"""
from prac_09.silver_service_taxi import SilverServiceTaxi

trip = SilverServiceTaxi('Hummer', 200, 2)
trip.drive(18)
print(trip)
print(f'${trip.get_fare():.2f}')
