# Day 19 - The Temperature Vault
# Min Stack with O(1) minimum lookup


class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, temperature):
        self.stack.append(temperature)

        if not self.min_stack:
            self.min_stack.append(temperature)
        else:
            current_min = min(self.min_stack[-1], temperature)
            self.min_stack.append(current_min)

    def pop(self):
        if not self.stack:
            print("Stack is empty")
            return None

        self.min_stack.pop()
        return self.stack.pop()

    def get_min(self):
        if not self.min_stack:
            print("Stack is empty")
            return None

        return self.min_stack[-1]


# Test the Min Stack

temperatures = [25, 18, 30, 12, 20]

vault = MinStack()

print("----- Temperature Vault -----")

for temperature in temperatures:
    vault.push(temperature)
    print("Pushed:", temperature, "| Current Minimum:", vault.get_min())

print("\nMinimum Temperature:", vault.get_min())

removed = vault.pop()
print("Popped:", removed)

print("Minimum Temperature after pop:", vault.get_min())

removed = vault.pop()
print("Popped:", removed)

print("Minimum Temperature after pop:", vault.get_min())
