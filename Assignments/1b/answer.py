import math

distance_km = 450
fuel_efficiency = 15
fuel_price = 1.20
average_speed = 80

travel_time_h = distance_km / average_speed
fuel_needed_liters = distance_km / fuel_efficiency
fuel_cost = fuel_needed_liters * fuel_price

print(f"Total Distance: {distance_km} km")
print(f"Estimated travel time: {math.ceil(travel_time_h)} hours")
print(f"Fuel needed: {fuel_needed_liters:.2f} liters")
print(f"Total fuel cost: ${fuel_cost:.2f}")