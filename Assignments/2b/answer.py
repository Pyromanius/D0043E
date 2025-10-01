import math


def calculate_travel_time(distance_km, average_speed):
    return math.ceil(distance_km / average_speed)


def calculate_fuel_needed(distance_km, fuel_efficiency):
    return (distance_km / fuel_efficiency)


def calculate_fuel_cost(fuel_needed, fuel_price):
    return (fuel_needed * fuel_price)


distance_km = math.ceil(float(input()))
fuel_efficiency = float(input())
fuel_price = float(input())
average_speed = float(input())

fuel_needed = calculate_fuel_needed(distance_km, fuel_efficiency)
travel_time = calculate_travel_time(distance_km, average_speed)

print(f"Total Distance: {distance_km} km")
print(f"Estimated Travel Time: {travel_time} hours")
print(f"Fuel Needed: {fuel_needed:.2f} liters")
print(f"Total Fuel Cost: ${calculate_fuel_cost(fuel_needed, fuel_price):.2f}")