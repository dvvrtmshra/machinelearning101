from sklearn.model_selection import train_test_split

X = [[10], [12], [14], [16], [18], [20], [22], [24]]
y = [20, 24, 28, 32, 36, 40, 44, 48]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

print("X_train:", X_train)
print("X_test:", X_test)
