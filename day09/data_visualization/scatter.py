import matplotlib.pyplot as plt

x = list(map(float, input("Enter x values: ").split()))
y = list(map(float, input("Enter y values: ").split()))

plt.scatter(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter Plot")
plt.show()
