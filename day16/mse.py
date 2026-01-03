# Mean Squared Error (from scratch)

actual = list(map(float, input("Enter actual values: ").split()))
predicted = list(map(float, input("Enter predicted values: ").split()))

n = len(actual)

if n != len(predicted):
    print("Lists must be of same length")
else:
    mse = sum((actual[i] - predicted[i]) ** 2 for i in range(n)) / n
    print("Mean Squared Error:", mse)
