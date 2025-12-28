# Random Data Generator & Analysis

import random
import matplotlib.pyplot as plt

n = int(input("Enter number of data points: "))

data = [random.randint(1, 100) for _ in range(n)]

print("Count:", len(data))
print("Min:", min(data))
print("Max:", max(data))
print("Mean:", sum(data) / len(data))

plt.hist(data, bins=10)
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Random Data Distribution")
plt.show()
