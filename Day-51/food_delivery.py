from dataclasses import dataclass, field
from enum import Enum
from itertools import count

class Status(str, Enum):
    PLACED="PLACED"; ACCEPTED="ACCEPTED"; PREPARING="PREPARING"
    PICKED_UP="PICKED_UP"; DELIVERED="DELIVERED"; CANCELLED="CANCELLED"

@dataclass
class User:
    user_id: int
    name: str

@dataclass
class Restaurant:
    restaurant_id: int
    name: str
    menu: dict

@dataclass
class Order:
    order_id: int
    user: User
    restaurant: Restaurant
    items: dict
    status: Status = Status.PLACED
    tracking: list = field(default_factory=list)

    @property
    def total(self):
        return sum(self.restaurant.menu[item] * qty for item, qty in self.items.items())

    def update_status(self, new_status):
        allowed = {
            Status.PLACED: {Status.ACCEPTED, Status.CANCELLED},
            Status.ACCEPTED: {Status.PREPARING, Status.CANCELLED},
            Status.PREPARING: {Status.PICKED_UP},
            Status.PICKED_UP: {Status.DELIVERED},
            Status.DELIVERED: set(), Status.CANCELLED: set()
        }
        if new_status not in allowed[self.status]:
            raise ValueError(f"Invalid status transition: {self.status} -> {new_status}")
        self.status = new_status
        self.tracking.append(new_status.value)

class Platform:
    def __init__(self):
        self.users, self.restaurants, self.orders = {}, {}, {}
        self.ids = count(1)

    def place_order(self, user, restaurant, items):
        if user not in self.users or restaurant not in self.restaurants:
            raise ValueError("Unknown user or restaurant")
        shop = self.restaurants[restaurant]
        if not items or any(k not in shop.menu for k in items):
            raise ValueError("Empty order or item not on menu")
        if any(not isinstance(q, int) or q <= 0 for q in items.values()):
            raise ValueError("Quantities must be positive integers")
        order = Order(next(self.ids), self.users[user], shop, items.copy())
        self.orders[order.order_id] = order
        return order

if __name__ == "__main__":
    app = Platform()
    app.users[1] = User(1, "Ramya")
    app.restaurants[10] = Restaurant(10, "Green Bowl", {"Veg Bowl": 120, "Paneer Wrap": 150})
    order = app.place_order(1, 10, {"Veg Bowl": 2, "Paneer Wrap": 1})
    print("Food Delivery Empire")
    print("Order ID:", order.order_id, "| Customer:", order.user.name)
    print("Restaurant:", order.restaurant.name, "| Total: ₹" + str(order.total))
    for status in [Status.ACCEPTED, Status.PREPARING, Status.PICKED_UP, Status.DELIVERED]:
        order.update_status(status)
    print("Tracking:", " -> ".join(order.tracking))
