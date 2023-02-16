import threading

# import "packages" from flask
from flask import render_template  # import render_template from "public" flask libraries
from flask_cors import CORS
# import "packages" from "this" project
from __init__ import app, db  # Definitions initialization
from api.apireal import mainData
from model.inventory import init_inventory
# setup App pages
from projects.projects import app_projects # Blueprint directory import projects definition

from model.users import initUsers
from api.inventory import inventory_bp
@app.errorhandler(404)  # catch for URL not found
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/')  # connects default URL to index() function
def index():
    return render_template("index.html")

@app.route('/stub/')  # connects /stub/ URL to stub() function
def stub():
    return render_template("stub.html")


@app.before_first_request

def init_db():
    with app.app_context():
        db.create_all()
        print("test")
        initUsers()
        init_inventory()


# this runs the application on the development server
if __name__ == "__main__":
    # change name for testing
    db.init_app(app)
    cors = CORS(app)
    app.run(debug=True, host="0.0.0.0", port="8080") 
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./volumes/sqlite.db"