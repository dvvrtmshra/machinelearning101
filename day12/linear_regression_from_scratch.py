# Single Variable Linear Regression (from scratch)

x = list(map(float, input("Enter x values: ").split()))
y = list(map(float, input("Enter y values: ").split()))

n = len(x)

mean_x = sum(x) / n
mean_y = sum(y) / n

num = 0
den = 0

for i in range(n):
    num += (x[i] - mean_x) * (y[i] - mean_y)
    den += (x[i] - mean_x) ** 2

m = num / den
b = mean_y - m * mean_x

print("Slope (m):", m)
print("Intercept (b):", b)

# Prediction
x_new = float(input("Enter x to predict y: "))
y_pred = m * x_new + b

print("Predicted y:", y_pred)
