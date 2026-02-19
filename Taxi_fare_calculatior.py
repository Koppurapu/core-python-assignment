
def calculate_fare(distance):
    base_fare = 50
    rate_per_km = 10
    return base_fare + (distance * rate_per_km)


# Input example
trips = [5, 10, 3]

total_fare = 0

# Calculate fare for each trip
for i, distance in enumerate(trips, start=1):
    fare = calculate_fare(distance)
    total_fare += fare
    print(f"Trip {i}: ${fare}")

# Print total fare
print(f"Total Fare: ${total_fare}")
