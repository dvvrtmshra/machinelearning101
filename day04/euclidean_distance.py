# Euclidean Distance (n-dimensional)

import math

point1 = list(map(float, input("Enter first point values: ").split()))
point2 = list(map(float, input("Enter second point values: ").split()))

if len(point1) != len(point2):
    print("Points must have same dimensions")
else:
    distance = math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))
    print("Euclidean Distance:", distance)
