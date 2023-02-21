from sqlalchemy import Column, Integer, String
from __init__ import db
import random


class InventoryEntry(db.Model):
    __tablename__ = "inventories"

    id = Column(Integer, primary_key=True)
    _username = Column(String(255), nullable=False)
    _inventory_name = Column(String(255), nullable=False)
    _quantity = Column(Integer, nullable=False)
    _price = Column(Integer, nullable=False)
    _cost = Column(Integer, nullable=False)
    _delivery = Column(Integer, nullable=False)
    _extra_notes = Column(String(255), nullable=False)

    def __init__(self, username, inventory_name, quantity, price, cost, delivery, extra_notes):
        self._username = username
        self._inventory_name = inventory_name
        self._quantity = quantity
        self._price = price
        self._cost = cost
        self._delivery = delivery
        self._extra_notes = extra_notes


    def __repr__(self):
        return (
            "<FitnessEntry(id='%s', username='%s', quantity='%s', price='%s', cost='%s', delivery='%s', extra_notes='%s')>"
            % (
                self.id,
                self.username,
                self.quantity,
                self.price,
                self.cost,
                self.delivery,
                self.extra_notes,
            )
        )


    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def inventory_name(self):
        return self._inventory_name

    @inventory_name.setter
    def inventory_name(self, value):
        self._inventory_name = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        self._cost = value

    @property
    def delivery(self):
        return self._delivery

    @delivery.setter
    def delivery(self, value):
        self._delivery = value

    @property
    def extra_notes(self):
        return self._extra_notes

    @extra_notes.setter
    def extra_notes(self, value):
        self._extra_notes = value

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "quantity": self.quantity,
            "price": self.price,
            "cost": self.cost,
            "delivery": self.delivery,
            "extra_notes": self.extra_notes,
            "inventory_name": self.inventory_name,
        }

def inventory_table_empty():
    return len(db.session.query(InventoryEntry).all()) == 0


def init_inventories():
    if not inventory_table_empty():
        return

    entry1 = InventoryEntry("Company A", "Product A", 2000, 150, 70, 150, "shipped")
    entry2 = InventoryEntry(
        "Company B", "Product B", 1700, 120, 50, 100, "out for pickup"
    )
    entry3 = InventoryEntry("Company C", "Product C", 1500, 200, 80, 200, "shipped")

    inventory_entries = [entry1, entry2, entry3]

    for entry in inventory_entries:
        try:
            db.session.add(entry)
            db.session.commit()
        except Exception as e:
            print("error while creating entries: " + str(e))
            db.session.rollback()