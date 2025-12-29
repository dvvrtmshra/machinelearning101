# Prediction using Simple Average

values = list(map(float, input("Enter past values: ").split()))

prediction = sum(values) / len(values)

print("Predicted next value:", prediction)
