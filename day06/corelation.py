# Correlation between two variables (Pearson)

import math

x = list(map(float, input("Enter first list: ").split()))
y = list(map(float, input("Enter second list: ").split()))

n = len(x)

if n != len(y):
    print("Lists must be of same length")
else:
    mean_x = sum(x) / n
    mean_y = sum(y) / n

    cov = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n)) / n
    std_x = math.sqrt(sum((xi - mean_x) ** 2 for xi in x) / n)
    std_y = math.sqrt(sum((yi - mean_y) ** 2 for yi in y) / n)

    correlation = cov / (std_x * std_y)

    print("Correlation:", correlation)
