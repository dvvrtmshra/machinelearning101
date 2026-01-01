from sklearn.linear_model import LinearRegression
import numpy as np

# Input data
x = np.array(list(map(float, input("Enter x values: ").split()))).reshape(-1, 1)
y = np.array(list(map(float, input("Enter y values: ").split())))

# Create model
model = LinearRegression()

# Train model
model.fit(x, y)

# Model parameters
print("Slope (m):", model.coef_[0])
print("Intercept (b):", model.intercept_)

# Prediction
x_new = float(input("Enter x to predict y: "))
y_pred = model.predict([[x_new]])

print("Predicted y:", y_pred[0])
