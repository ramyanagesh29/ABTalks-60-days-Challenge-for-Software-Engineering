# Day 22 - The Theme Park FastPass Simulator


class ThemeParkQueue:

    def __init__(self):
        self.normal_queue = []
        self.vip_queue = []

    def join_queue(self, visitor, vip=False):

        if vip:
            self.vip_queue.append(visitor)
            print(visitor, "joined VIP queue")
        else:
            self.normal_queue.append(visitor)
            print(visitor, "joined normal queue")

    def process_next(self):

        # VIP visitors have priority
        if self.vip_queue:
            visitor = self.vip_queue.pop(0)
            print("Processing VIP visitor:", visitor)
            return visitor

        # Process normal visitors if no VIP is waiting
        if self.normal_queue:
            visitor = self.normal_queue.pop(0)
            print("Processing normal visitor:", visitor)
            return visitor

        print("No visitors waiting")
        return None

    def display_queues(self):

        print("\n----- Current Queues -----")
        print("VIP Queue:", self.vip_queue)
        print("Normal Queue:", self.normal_queue)


# Create the theme park scheduler

park = ThemeParkQueue()

print("===== Theme Park FastPass Simulator =====\n")

# Visitors arrive
park.join_queue("Ramya")
park.join_queue("Rahul")
park.join_queue("Anu", vip=True)
park.join_queue("Kiran")
park.join_queue("Priya", vip=True)

park.display_queues()

print("\n----- Processing Visitors -----")

park.process_next()
park.process_next()
park.process_next()
park.process_next()
park.process_next()

park.display_queues()
