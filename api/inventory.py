from flask import Blueprint, request
from flask_restful import Api, Resource, reqparse
from __init__ import db
from model.inventory import InventoryEntry

inventory_bp = Blueprint("inventory", __name__)
inventory_api = Api(inventory_bp)


class InventoryAPI(Resource):
    def get(self):
        company = request.args.get("company")
        entry = db.session.query(InventoryEntry).filter_by(_company=company).all()
        print("abc" + str(company))
        if len(entry) != 0:
            return [e.to_dict() for e in entry]
        return {"error": "company not found"}, 404

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("company", required=True, type=str)
        parser.add_argument("action", required=True, type=int)
        parser.add_argument("quantity", required=True, type=int)
        parser.add_argument("extra_notes", required=True, type=str)
        parser.add_argument("inventory_name", required=True, type=str)
        args = parser.parse_args()

        entry = InventoryEntry(
            args["company"],
            args["inventory_name"],
            args["action"],
            args["quantity"],
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
        parser.add_argument("action", required=False, type=int)
        parser.add_argument("quantity", required=False, type=int)
        parser.add_argument("extra_notes", required=False, type=str)
        parser.add_argument("inventory_name", required=True, type=str)
        args = parser.parse_args()

        try:
            entry = db.session.query(InventoryEntry).get(args["id"])
            if entry:
                if args["action"]:
                    entry.calories = args["action"]
                if args["quantity"]:
                    entry.protein = args["quantity"]
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


inventory_api.add_resource(InventoryAPI, "/inventory")