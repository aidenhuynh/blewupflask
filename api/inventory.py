from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource, reqparse
from __init__ import db
from model.inventory import InventoryEntry

inventories_bp = Blueprint("inventories", __name__)
inventories_api = Api(inventories_bp)

class InventoryAPI(Resource):
    def get(self):
        username = request.args.get("username")
        entry = db.session.query(InventoryEntry).filter_by(_username=username).all()
        print("abc" + str(username))
        if len(entry) != 0:
            return [e.to_dict() for e in entry]
        return {"error": "user not found"}, 404

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True, type=str)
        parser.add_argument("quantity", required=True, type=int)
        parser.add_argument("price", required=True, type=int)
        parser.add_argument("cost", required=True, type=int)
        parser.add_argument("delivery", required=True, type=int)
        parser.add_argument("extra_notes", required=True, type=str)
        parser.add_argument("inventory_name", required=True, type=str)
        args = parser.parse_args()

        entry = InventoryEntry(
            args["username"],
            args["inventory_name"],
            args["quantity"],
            args["price"],
            args["cost"],
            args["delivery"],
            args["extra_notes"],
        )
        try:
            db.session.add(entry)
            db.session.commit()
            return entry.to_dict(), 201
        except Exception as e:
            db.session.rollback()
            return {"error": f"server error: {e}"}, 500

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", required=True, type=int)
        parser.add_argument("quantity", required=False, type=int)
        parser.add_argument("price", required=False, type=int)
        parser.add_argument("cost", required=False, type=int)
        parser.add_argument("delivery", required=False, type=int)
        parser.add_argument("extra_notes", required=False, type=str)
        parser.add_argument("inventory_name", required=True, type=str)
        args = parser.parse_args()

        try:
            entry = db.session.query(InventoryEntry).get(args["id"])
            if entry:
                if args["quantity"]:
                    entry.quantity = args["quantity"]
                if args["price"]:
                    entry.price = args["price"]
                if args["cost"]:
                    entry.cost = args["cost"]
                if args["delivery"]:
                    entry.delivery = args["delivery"]
                if args["extra_notes"]:
                    entry.extra_notes = args["extra_notes"]
                if args["inventory_name"]:
                    entry.extra_notes = args["inventory_name"]
                db.session.commit()
                return entry.to_dict()
            else:
                return {"error": "entry not found"}, 404
        except Exception as e:
            db.session.rollback()
            return {"error": f"server error: {e}"}, 500

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", required=True, type=int)
        args = parser.parse_args()

        try:
            entry = db.session.query(InventoryEntry).get(args["id"])
            if entry:
                db.session.delete(entry)
                db.session.commit()
                return entry.to_dict()
            else:
                return {"error": "entry not found"}, 404
        except Exception as e:
            db.session.rollback()
            return {"error": f"server error: {e}"}, 500


inventories_api.add_resource(InventoryAPI, "/inventory")