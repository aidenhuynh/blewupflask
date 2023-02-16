from sqlalchemy import Column, Integer, String
from __init__ import db
import random


class InventoryEntry(db.Model):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True)
    _company = Column(String(255), nullable=False)
    _product = Column(String(255), nullable=False)
    _inventory_name = Column(String(255), nullable=False)
    _action = Column(String, nullable=False)
    _quantity = Column(Integer, nullable=False)
    _status = Column(String(255), nullable=False)

    def __init__(self, company, product, inventory_name, action, quantity, status):
        self._company = company
        self._product = product
        self._inventory_name = inventory_name
        self._action = action
        self._quantity = quantity
        self._status = status

    def __repr__(self):
        return (
            "<InventoryEntry(id='%s', company='%s', product='%s', inventory_name='%s', action='%s', quantity='%s', status='%s')>"
            % (
                self.id,
                self.company,
                self.product,
                self.inventory_name,
                self.action,
                self.quantity,
                self.status,
            )
        )

    @property
    def product(self):
        return self._product

    @product.setter
    def product_set(self, value):
        self._product = value

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
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, company):
        self._company = company

    def to_dict(self):
        return {
            "id": self.id,
            "company": self.company,
            "product": self.product,
            "action": self.action,
            "quantity": self.quantity,
            "status": self.status,
            "inventory_name": self.inventory_name,
        }


def inventory_table_empty():
    return len(db.session.query(InventoryEntry).all()) == 0


def init_inventory():
    if not inventory_table_empty():
        return

    entry1 = InventoryEntry("Company A", "Product A", "Cargo", "Shipped", 150, "out for shipment")
    entry2 = InventoryEntry("Company B", "Product B","Cargo", "Delivery", 250, "out for delivery")
    entry3 = InventoryEntry("Company C", "Product C", "Cargo", "Packaged", 350, "ready for delivery")

    inventory_entries = [entry1, entry2, entry3]

    for entry in inventory_entries:
        try:
            db.session.add(entry)
            db.session.commit()
        except Exception as e:
            print("error while creating entries: " + str(e))
            db.session.rollback()