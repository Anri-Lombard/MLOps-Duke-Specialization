import random
from geopy.distance import geodesic

def calculate_distance(point1, point2):
    """
    Calculate the Haversine distance between two points.
    """
    return geodesic(point1, point2).kilometers

def nearest_neighbor(cities, current_city):
    """
    Find the city closest to the current city.
    """
    return min(cities, key=lambda city: calculate_distance(current_city, city))

def travelling_salesman(cities, start):
    """
    Solve the Traveling Salesman Problem using the Nearest Neighbor heuristic.
    """
    path = [start]
    while cities:
        closest_city = nearest_neighbor(cities, path[-1])
        if closest_city != start:  # Add this condition to avoid adding the start city twice
            path.append(closest_city)
        cities.remove(closest_city)
    return path

# Define the coordinates of the cities
cities = {
    'Cape Town': (-33.9249, 18.4241),
    'Johannesburg': (-26.2041, 28.0473),
    'Durban': (-29.8587, 31.0218),
    'Pretoria': (-25.7479, 28.2293),
    'Port Elizabeth': (-33.9608, 25.6022)
}

# Choose a random city to start
start = random.choice(list(cities.values()))

# Find the best route
best_route = travelling_salesman(list(cities.values()), start)

# Print the best route
print(f"The best route to visit all the cities is from a random starting city is:")
for city in best_route:
    print([name for name, coord in cities.items() if coord == city][0])

# Calculate the total distance
total_distance = sum([calculate_distance(best_route[i], best_route[i+1]) for i in range(len(best_route)-1)])

print(f"The total distance of this route is: {total_distance} kilometers")
