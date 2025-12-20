# Min-Max Normalization

numbers = list(map(float, input("Enter numbers separated by space: ").split()))

min_val = min(numbers)
max_val = max(numbers)

normalized = []

for x in numbers:
    norm = (x - min_val) / (max_val - min_val)
    normalized.append(norm)

print("Original Data:", numbers)
print("Normalized Data:", normalized)
