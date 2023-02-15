from sqlalchemy import Column, Integer, String
from __init__ import db
import random


class InventoryEntry(db.Model):
    __tablename__ = "Inventory"

    id = Column(Integer, primary_key=True)
    _company = Column(String(255), nullable=False)
    _inventory_name = Column(String(255), nullable=False)
    _action = Column(Integer, nullable=False)
    _quantity = Column(Integer, nullable=False)
    _extra_notes = Column(String(255), nullable=False)

    def __init__(self, company, inventory_name, action, quantity, extra_notes):
        self._company = company
        self._inventory_name = inventory_name
        self._action = action
        self._quantity = quantity
        self._extra_notes = extra_notes

    def __repr__(self):
        return (
            "<InventoryEntry(id='%s', company='%s', inventory_name='%s', action='%s', quantity='%s', extra_notes='%s')>"
            % (
                self.id,
                self.company,
                self.inventory_name,
                self.action,
                self.quantity,
                self.extra_notes,
            )
        )

    @property
    def company(self):
        return self.company

    @company.setter
    def company(self, value):
        self._company = value

    @property
    def inventory_name(self):
        return self._inventory_name

    @inventory_name.setter
    def inventory_name(self, value):
        self._inventory_name = value

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    @property
    def extra_notes(self):
        return self._extra_notes

    @extra_notes.setter
    def extra_notes(self, value):
        self._extra_notes = value

    def to_dict(self):
        return {
            "id": self.id,
            "company": self.company,
            "action": self.action,
            "quantity": self.quantity,
            "extra_notes": self.extra_notes,
            "inventory_name": self.inventory_name,
        }


def inventory_table_empty():
    return len(db.session.query(InventoryEntry).all()) == 0


def init_inventory():
    if not inventory_table_empty():
        return

    entry1 = InventoryEntry("Company A", "Product A", "Shipped", 150, "out for delivery")
    entry2 = InventoryEntry("Company B", "Product B", "Delivered", 200, "out for pick-up")
    entry3 = InventoryEntry("Company C", "Product C", "Stored", 250, "in for storage")

    inventory_entries = [entry1, entry2, entry3]

    for entry in inventory_entries:
        try:
            db.session.add(entry)
            db.session.commit()
        except Exception as e:
            print("error while creating entries: " + str(e))
            db.session.rollback()
