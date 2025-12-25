# Data Summary Tool

numbers = list(map(float, input("Enter numbers separated by space: ").split()))

count = len(numbers)
minimum = min(numbers)
maximum = max(numbers)
mean = sum(numbers) / count

print("Count:", count)
print("Minimum:", minimum)
print("Maximum:", maximum)
print("Mean:", mean)
