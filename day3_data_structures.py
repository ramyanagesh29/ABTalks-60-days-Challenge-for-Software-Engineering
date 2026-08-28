numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Sum
total = 0
for number in numbers:
    total = total + number

# Maximum and Minimum
max_value = numbers[0]
min_value = numbers[0]

for number in numbers:
    if number > max_value:
        max_value = number

    if number < min_value:
        min_value = number

# Frequency
frequency = {}

for number in numbers:
    if number in frequency:
        frequency[number] = frequency[number] + 1
    else:
        frequency[number] = 1

print("Sum:", total)
print("Maximum:", max_value)
print("Minimum:", min_value)
print("Frequency:", frequency)

# Bonus: Reverse without built-in reverse functions
reversed_list = []

for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

print("Reversed list:", reversed_list)
