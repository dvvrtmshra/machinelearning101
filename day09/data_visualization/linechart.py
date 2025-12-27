import matplotlib.pyplot as plt

data = list(map(float, input("Enter numbers: ").split()))

plt.plot(data)
plt.xlabel("Index")
plt.ylabel("Value")
plt.title("Line Plot")
plt.show()
