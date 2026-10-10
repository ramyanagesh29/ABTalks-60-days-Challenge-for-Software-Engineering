# Day 45 — The Emergency Room Simulator

A min-heap prioritizes lower severity numbers first (1 = most urgent). A sequence number
preserves arrival order when two patients have the same severity.

- Add patient: O(log N)
- Treat next patient: O(log N)
- Storage: O(N)

This is an educational simulation, not a clinical triage system. Real patient prioritization
must follow validated protocols and qualified medical judgment.

Run: `python day45_emergency_room.py`
