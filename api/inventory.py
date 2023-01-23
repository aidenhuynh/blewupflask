from flask import Flask, request
from .. import db
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class InventoryAPI(Resource):
    def post(self):
        body = request.get_json()
        date = body.get('date')
        action = body.get('action')
        user = body.get('user')
        item = body.get('item')
        quantity = body.get('quantity')

        # Create a new entry in the database
        new_entry = {'date': date, 'action': action, 'user': user, 'item': item, 'quantity': quantity}
        inventory_list.append(new_entry)

        return {'message': 'Inventory entry added successfully'}, 201

    def get(self):
        return {'inventory': inventory_list}

    def put(self, id):
        body = request.get_json()
        date = body.get('date')
        action = body.get('action')
        user = body.get('user')
        item = body.get('item')
        quantity = body.get('quantity')

        # Update the entry in the database
        inventory_list[id] = {'date': date, 'action': action, 'user': user, 'item': item, 'quantity': quantity}

        return {'message': 'Inventory entry updated successfully'}

    def delete(self, id):
        # Delete the entry from the database
        del inventory_list[id]

        return {'message': 'Inventory entry deleted successfully'}

api.add_resource(InventoryAPI, '/inventory/<int:id>')
