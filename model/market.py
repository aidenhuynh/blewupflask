from sqlalchemy import Column, Integer, String
from __init__ import db
import random


class MarketEntry(db.Model):
    __tablename__ = "Market"

    id = Column(Integer, primary_key=True)
    _date = Column(String(255), nullable=False)
    _market_name = Column(String(255), nullable=False)
    _product = Column(Integer, nullable=False)
    _cost = Column(Integer, nullable=False)
    _stock = Column(String(255), nullable=False)

    def __init__(self, date, market_name, product, cost, stock):
        self._date = date
        self._market_name = market_name
        self._product = product
        self._cost = cost
        self._stock = stock

    def __repr__(self):
        return (
            "<MarketEntry(id='%s', date='%s', market_name='%s', product='%s', cost='%s', stock='%s')>"
            % (
                self.id,
                self.date,
                self.market_name,
                self.product,
                self.cost,
                self.stock,
            )
        )

    @property
    def date(self):
        return self.date

    @date.setter
    def date(self, value):
        self._date = value

    @property
    def market_name(self):
        return self._market_name

    @market_name.setter
    def market_name(self, value):
        self._market_name = value

    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, value):
        self._product = value

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        self._cost = value

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, value):
        self._stock = value

    def to_dict(self):
        return {
            "id": self.id,
            "product": self.product,
            "date": self.date,
            "cost": self.cost,
            "stock": self.stock,
            "market_name": self.market_name,
        }


def market_table_empty():
    return len(db.session.query(MarketEntry).all()) == 0


def init_market():
    if not market_table_empty():
        return

    entry1 = MarketEntry("Company A", "Product A", "Shipped", 150, "out for delivery")
    entry2 = MarketEntry("Company B", "Product B", "Delivered", 200, "out for pick-up")
    entry3 = MarketEntry("Company C", "Product C", "Stored", 250, "in for storage")

    market_entries = [entry1, entry2, entry3]

    for entry in market_entries:
        try:
            db.session.add(entry)
            db.session.commit()
        except Exception as e:
            print("error while creating entries: " + str(e))
            db.session.rollback()
