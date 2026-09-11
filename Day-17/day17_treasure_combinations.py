# Day 17 - Treasure Chest Combination Generator

def generate_subsets(gems):
    result = []
    current = []

    def backtrack(index):
        # Base case: all gems have been considered
        if index == len(gems):
            result.append(current.copy())
            return

        # Choice 1: Do not take the current gem
        backtrack(index + 1)

        # Choice 2: Take the current gem
        current.append(gems[index])
        backtrack(index + 1)

        # Backtrack: remove the gem
        current.pop()

    backtrack(0)

    return result


gems = ["Ruby", "Diamond", "Emerald"]

combinations = generate_subsets(gems)

print("----- Treasure Chest Combination Generator -----")
print("Gems:", gems)

print("\nAll possible combinations:")

for combination in combinations:
    print(combination)

print("\nTotal combinations:", len(combinations))
