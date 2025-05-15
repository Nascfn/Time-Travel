# This program calculates cost, chooses a destination, and a year for the time traveler to travel to

# Imports
import datetime as dt
from decimal import Decimal
from random import randint, choice
from custom_module import generate_time_trave_message

# Getting today's date
todays_date = dt.date.today()
current_time = dt.datetime.now().time()

# Generate random number for the target year
target_year = randint(10, 5000)

# Calculate cost based on difference from target year and current year along with a fixed cost
base_cost = Decimal('50000.00')
total_cost = base_cost + (abs(Decimal(str(todays_date.year)) - Decimal(str(target_year))) * 123)
total_cost = round(total_cost, 2)

# List of possible places for the traveler to visit and choose a random one
possible_destinations = ["Christ the Redeemer", "The Coca Cola Factory", "Great Wall of China", "Taj Mahal", "Great Pyramid of Giza", "Statue of Zeus at Olympia", "Colossus of Rhodes", "Old Trafford"]
chosen_destination = choice(possible_destinations)

# Calls function that was created in another file
generate_time_trave_message(target_year, chosen_destination, total_cost)