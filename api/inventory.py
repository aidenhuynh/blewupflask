from flask import Blueprint, request
from flask_restful import Api, Resource, reqparse
from .. import db
from ..model.inventory import InventoryEntry

table_bp = Blueprint("inventory", __name__)
table_api = Api(table_bp)

class InventoryAPI(Resource):
    def get(self):
        id = request.args.get("id")
        entry = db.session.query(InventoryEntry).get(id)
        if entry:
            return entry.to_dict()
        return {"message": "entry not found"}, 404

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("product_name", required=True, type=str)
        parser.add_argument("product_description", required=True, type=str)
        parser.add_argument("quantity", required=True, type=int)
        parser.add_argument("price", required=True, type=float)
        args = parser.parse_args()

        entry = InventoryEntry(
            product_name=args["product_name"],
            product_description=args["product_description"],
            quantity=args["quantity"],
            price=args["price"],
        )

        try:
            db.session.add(entry)
            db.session.commit()
            return entry.to_dict(), 201
        except Exception as e:
            db.session.rollback()
            return {"message": f"server error: {e}"}, 500

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", required=True, type=int)
        parser.add_argument("product_name", type=str)
        parser.add_argument("product_description", type=str)
        parser.add_argument("quantity", type=int)
        parser.add_argument("price", type=float)
        args = parser.parse_args()

        try:
            entry = db.session.query(InventoryEntry).get(args["id"])
            if entry:
                if args["product_name"]:
                    entry.product_name = args["product_name"]
                if args["product_description"]:
                    entry.product_description = args["product_description"]
                if args["quantity"]:
                    entry.quantity = args["quantity"]
                if args["price"]:
                    entry.price = args["price"]
                db.session.commit()
                return entry.to_dict()
            else:
                return {"message": "entry not found"}, 404
        except Exception as e:
            db.session.rollback()
            return {"message": f"server error: {e}"}, 500

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
                return {"message": "entry not found"}, 404
        except Exception as e:
            db.session.rollback()
            return {"message": f"server error: {e}"}, 500


class InventoryListAPI(Resource):
    def get(self):
        try:
            entries = db.session.query(InventoryEntry).all()
            return [entry.to_dict() for entry in entries]
        except Exception as e:
            db.session.rollback()
            return {"message": f"server error: {e}"}, 500

    def delete(self):
        try:
            db.session.query(InventoryEntry).delete()
            db.session.commit()
            return []
        except Exception as e:
            db.session.rollback()
            return {"message": f"server error: {e}"}, 500


table_api.add_resource(InventoryAPI, "/inventory")
table_api.add_resource(InventoryListAPI, "/inventory/list")
