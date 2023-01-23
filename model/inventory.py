from sqlalchemy import Column, Integer, String, Boolean
from .. import db


class Inventory:
    def __init__(self, date, action, user, item, quantity):
        self.date = date
        self.action = action
        self.user = user
        self.item = item
        self.quantity = quantity
        
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        self._date = value
        
    @property
    def action(self):
        return self._action
    
    @action.setter
    def action(self, value):
        self._action = value
        
    @property
    def user(self):
        return self._user
    
    @user.setter
    def user(self, value):
        self._user = value
        
    @property
    def item(self):
        return self._item
    
    @item.setter
    def item(self, value):
        self._item = value
    
    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, value):
        self._quantity = value


inventory1 = Inventory(date='2022-01-01', action='purchase', user='John Doe', item='item1', quantity=10)
inventory2 = Inventory(date='2022-01-02', action='purchase', user='Jane Doe', item='item2', quantity=5)
inventory3 = Inventory(date='2022-01-03', action='sale', user='John Smith', item='item1', quantity=2)
inventory4 = Inventory(date='2022-01-04', action='purchase', user='Jane Smith', item='item3', quantity=7)
inventory5 = Inventory(date='2022-01-05', action='sale', user='Bob', item='item2', quantity=3)

db.session.add(inventory1)
db.session.add(inventory2)
db.session.add(inventory3)
db.session.add(inventory4)
db.session.add(inventory5)
db.session.commit()