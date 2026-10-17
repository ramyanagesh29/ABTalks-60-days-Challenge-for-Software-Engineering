# Architecture Notes

User 1 --- places ---> Order --- belongs to ---> Restaurant
Restaurant owns a menu (item and price); Order stores quantities, total, status and tracking.

Potential API routes: POST /orders, GET /orders/{id}, PATCH /orders/{id}/status.
In production, persist state transactionally and emit events for notifications/tracking.
