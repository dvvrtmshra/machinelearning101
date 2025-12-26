# CSV Data Loader + Basic Analysis

import csv

values = []

with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        values.append(float(row["value"]))

count = len(values)
minimum = min(values)
maximum = max(values)
mean = sum(values) / count

print("Count:", count)
print("Minimum:", minimum)
print("Maximum:", maximum)
print("Mean:", mean)
