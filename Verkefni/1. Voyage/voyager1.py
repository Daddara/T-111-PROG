import datetime

MILES_FROM_SUN = 16637000000
MILES_PER_HOUR = 38241
KM_IN_MILE = 1.609344
AU_IN_MILE = 92955887.6
HOURS_IN_DAY = 24

number_of_days = int(input("Number of days after 9/25/09: "))

'''Calculates total travel in miles'''
miles_per_day = (number_of_days*(MILES_PER_HOUR*HOURS_IN_DAY))

'''Calculates total distance'''
total_miles_from_sun = (MILES_FROM_SUN+miles_per_day)
total_km_from_sun = (total_miles_from_sun*KM_IN_MILE)
total_au_from_sun = (total_miles_from_sun/AU_IN_MILE)

print("Miles from the sun:", total_miles_from_sun)
print("Kilometers from the sun:", round(total_km_from_sun))
print("AU from the sun:", round(total_au_from_sun))