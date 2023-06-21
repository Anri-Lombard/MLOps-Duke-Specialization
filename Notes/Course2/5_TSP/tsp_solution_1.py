from itertools import permutations
from geopy.distance import geodesic

def calculate_distance(point1, point2):
    """
    Calculate the Haversine distance between two points.
    """
    return geodesic(point1, point2).kilometers

def total_distance(points):
    """
    Calculate the total distance of the path.
    """
    return sum([calculate_distance(point, points[index + 1]) for index, point in enumerate(points[:-1])])

def travelling_salesman(points):
    """
    Finds the shortest route to visit all the cities by trying all the permutations.
    """
    min_distance = float('inf')
    best_route = None

    for perm in permutations(points):
        current_distance = total_distance(perm)
        if current_distance < min_distance:
            min_distance = current_distance
            best_route = perm

    return best_route, min_distance

# Define the coordinates of the cities
cities = {
    'Cape Town': (-33.9249, 18.4241),
    'Johannesburg': (-26.2041, 28.0473),
    'Durban': (-29.8587, 31.0218),
    'Pretoria': (-25.7479, 28.2293),
    'Port Elizabeth': (-33.9608, 25.6022)
}

# Find the best route
best_route, min_distance = travelling_salesman(list(cities.values()))

# Print the best route
print("The best route to visit all the cities is:")
for city in best_route:
    print([name for name, coord in cities.items() if coord == city][0])

print(f"The total distance of this route is: {min_distance} kilometers")
