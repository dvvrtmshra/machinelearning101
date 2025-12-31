import numpy as np

# Input data
x = np.array(list(map(float, input("Enter x values: ").split())))
y = np.array(list(map(float, input("Enter y values: ").split())))

# Mean values
mean_x = np.mean(x)
mean_y = np.mean(y)

# Slope (m) and Intercept (b)
m = np.sum((x - mean_x) * (y - mean_y)) / np.sum((x - mean_x) ** 2)
b = mean_y - m * mean_x

print("Slope (m):", m)
print("Intercept (b):", b)

# Prediction
x_new = float(input("Enter x to predict y: "))
y_pred = m * x_new + b

print("Predicted y:", y_pred)
