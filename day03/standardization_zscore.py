# Standardization (Z-score)

import math

numbers = list(map(float, input("Enter numbers separated by space: ").split()))

n = len(numbers)

# Mean
mean = sum(numbers) / n

# Standard Deviation
variance = sum((x - mean) ** 2 for x in numbers) / n
std_dev = math.sqrt(variance)

standardized = []

for x in numbers:
    z = (x - mean) / std_dev
    standardized.append(z)

print("Original Data:", numbers)
print("Mean:", mean)
print("Standard Deviation:", std_dev)
print("Standardized Data:", standardized)
