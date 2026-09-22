def contains_duplicate_within_k(events, k):
    last_seen = {}

    for index, event in enumerate(events):
        if event in last_seen and index - last_seen[event] <= k:
            return True, event, last_seen[event] + 1, index + 1
        last_seen[event] = index

    return False, None, None, None


events = [
    "POST:Buy now!",
    "POST:Hello everyone",
    "POST:New product today",
    "POST:Buy now!",
    "POST:Welcome to our page"
]
k = 3

result, event, first_position, second_position = contains_duplicate_within_k(events, k)

print("----- Social Media Fraud Detector -----")
print("Activity window K:", k)
print("Events:")
for index, activity in enumerate(events, start=1):
    print(index, "->", activity)

print("\nSuspicious repeated activity:", result)
if result:
    print("Repeated activity:", event)
    print("First position:", first_position)
    print("Second position:", second_position)
    print("Distance:", second_position - first_position)
