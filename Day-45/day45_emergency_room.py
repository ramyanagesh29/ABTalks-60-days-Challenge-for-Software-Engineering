import heapq
from itertools import count

class EmergencyRoom:
    # Severity 1 is most urgent; severity 5 is least urgent.
    def __init__(self):
        self.heap = []
        self.sequence = count()

    def add_patient(self, name, severity, reason):
        if severity not in range(1, 6):
            raise ValueError("Severity must be from 1 to 5.")
        heapq.heappush(self.heap, (severity, next(self.sequence), name, reason))

    def treat_next(self):
        if not self.heap:
            return None
        severity, _, name, reason = heapq.heappop(self.heap)
        return {"name": name, "severity": severity, "reason": reason}

if __name__ == "__main__":
    room = EmergencyRoom()
    room.add_patient("Asha", 3, "Fracture")
    room.add_patient("Ravi", 1, "Breathing difficulty")
    room.add_patient("Meena", 2, "Severe bleeding")
    room.add_patient("Kiran", 3, "High fever")
    print("Emergency Room Simulator")
    while room.heap:
        print(room.treat_next())
