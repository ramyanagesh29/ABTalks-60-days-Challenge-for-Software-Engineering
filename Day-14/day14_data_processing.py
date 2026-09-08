# Day 14 - Mini Data Processing System

# Dataset: Simulated user activity data
data = [10, 25, 10, 30, 25, 40, 10, 35, 30, 25]

# 1. Total number of records
total_records = len(data)

# 2. Calculate total
total = 0

for number in data:
    total += number

# 3. Calculate average
average = total / total_records

# 4. Find maximum and minimum values
maximum = data[0]
minimum = data[0]

for number in data:
    if number > maximum:
        maximum = number

    if number < minimum:
        minimum = number

# 5. Use hashing to count frequency
frequency = {}

for number in data:
    frequency[number] = frequency.get(number, 0) + 1

# 6. Find the most frequent value
most_frequent = data[0]
highest_count = 0

for number, count in frequency.items():
    if count > highest_count:
        highest_count = count
        most_frequent = number

# Display results
print("----- Data Processing Report -----")

print("Dataset:", data)
print("Total Records:", total_records)
print("Total:", total)
print("Average:", average)
print("Maximum Value:", maximum)
print("Minimum Value:", minimum)

print("\nFrequency Analysis:")

for number, count in frequency.items():
    print(number, "appears", count, "times")

print("\nMost Frequent Value:", most_frequent)
print("Highest Frequency:", highest_count)
