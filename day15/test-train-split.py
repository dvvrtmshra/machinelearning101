# Train-Test Split (from scratch)

data = [10, 12, 14, 16, 18, 20, 22, 24]
labels = [20, 24, 28, 32, 36, 40, 44, 48]

split_ratio = 0.75
split_index = int(len(data) * split_ratio)

x_train = data[:split_index]
x_test = data[split_index:]

y_train = labels[:split_index]
y_test = labels[split_index:]

print("Training data:", x_train)
print("Testing data:", x_test)
