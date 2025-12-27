import matplotlib.pyplot as plt

labels = ["A", "B", "C", "D"]
values = list(map(float, input("Enter 4 values: ").split()))

plt.bar(labels, values)
plt.xlabel("Category")
plt.ylabel("Value")
plt.title("Bar Chart")
plt.show()
