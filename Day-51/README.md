# Day 51 — Food Delivery Empire

Entities: User, Restaurant, Order. `Platform` validates and creates orders.
Flow: PLACED -> ACCEPTED -> PREPARING -> PICKED_UP -> DELIVERED.
The code validates menu items and positive quantities, calculates totals, and rejects invalid status transitions.

This is an in-memory learning simulation. A production system needs persistent storage, authentication,
payments, inventory checks, idempotency, monitoring, and reliable event handling.

Run: `python food_delivery.py`
