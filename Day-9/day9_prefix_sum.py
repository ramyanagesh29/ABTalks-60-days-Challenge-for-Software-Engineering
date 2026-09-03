numbers = [3, 2, 7, 4, 1]
queries = [(1, 3), (0, 2), (2, 4)]
print("Brute Force Results:")
for left, right in queries:
  total = 0

for index in range(left, right + 1):

    total = total + numbers[index]

print("Query", (left, right), "=", total)


print("\nPrefix Sum Results:")

prefix = [0]

for number in numbers:
  new_sum = number + prefix[-1]
  prefix.append(new_sum)

print("Prefix Array:", prefix)

for left, right in queries:
  result = prefix[right + 1] - prefix[left]

print("Query", (left, right), "=", result)
