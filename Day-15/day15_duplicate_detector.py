#Brute Force 
import time

numbers = [10, 20, 30, 20]

start = time.time()

duplicate_found = False

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            print("Duplicate found:", numbers[i])
            duplicate_found = True

end = time.time()

print("Brute Force Execution Time:", end - start)

# Complexity: O(N²) time, O(1) extra space.

#Optimized — Set
import time

numbers = [10, 20, 30, 20]

start = time.time()

seen = set()
duplicate_found = False

for number in numbers:
    if number in seen:
        print("Duplicate found:", number)
        duplicate_found = True
    else:
        seen.add(number)

end = time.time()

print("Set Execution Time:", end - start)

#Complexity: O(N) average time, O(N) space.

# Large Dataset
numbers = list(range(1000000))
numbers.append(numbers[500000])
