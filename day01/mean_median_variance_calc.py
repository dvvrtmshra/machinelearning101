# Mean, Median, Variance Calculator

numbers = list(map(float, input("Enter numbers separated by space: ").split()))

n = len(numbers)

# Mean
mean = sum(numbers) / n

# Median
numbers.sort()
if n % 2 == 0:
    median = (numbers[n//2 - 1] + numbers[n//2]) / 2
else:
    median = numbers[n//2]

# Variance
variance = sum((x - mean) ** 2 for x in numbers) / n

print("Mean:", mean)
print("Median:", median)
print("Variance:", variance)
