import threading
# import "packages" from flask
from flask import render_template  # import render_template from "public" flask libraries
from flask import Flask, request, jsonify
import sqlite3
import phonenumbers
from phonenumbers import geocoder, timezone
import datetime
from flask_cors import CORS
# import "packages" from "this" project
from __init__ import app, db  # Definitions initialization
from api.apireal import mainData
# setup App pages
from projects.projects import app_projects # Blueprint directory import projects definition
from model.users import initUsers
from api.user import user_api
from model.inventory import init_inventories



from api.inventory import inventories_bp
app.register_blueprint(user_api)
app.register_blueprint(inventories_bp)
app.register_blueprint(mainData)

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

# @app.before_first_request
# def activate_job():
    # with app.app_context():
        # db.create_all()
        # print("test")
        # initUsers()
        # initUsers()
        # init_inventories()

@app.route('/api/phone')
def phone():
    conn = sqlite3.connect('api/sqlites.db')
    c = conn.cursor()
    c.execute("SELECT * FROM phone")
    rows = c.fetchall()
    conn.close()

    data = []
    for row in rows:
        data.append({
            "user_id": row[0],
            "phone_number": row[1],
            "location": row[2],
            "timezone": row[3],
            "time": row[4]
        })

    return jsonify(data)

@app.route('/submit', methods=['POST'])
def submit():
    user_id = request.form['user_id']
    number = request.form['phone_number']

    # Run algorithm to find location and timezone of phone number
    ch_number = phonenumbers.parse(number, "CH")
    location = geocoder.description_for_number(ch_number, "en")
    givenPN = phonenumbers.parse(number, "CH")
    timezoneOfPN = timezone.time_zones_for_number(givenPN)
    timezone1 = timezoneOfPN[0] if timezoneOfPN else None
    now = datetime.datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M:%S")

    # Save the data to the database
    conn = sqlite3.connect('api/sqlites.db')
    c = conn.cursor()
    c.execute("INSERT INTO phone (user_id, phone_number, location, timezone, time) VALUES (?, ?, ?, ?, ?)", (user_id, number, location, timezone1, time))
    conn.commit()
    conn.close()

    return "Data has been submitted successfully."

if __name__ == "__main__":
    db.init_app(app)
    # change name for testing
    from flask_cors import CORS
    cors = CORS(app, support_credentials=True)
    app.run(debug=True) 
    
toptext = Flask(__name__)

toptext.config['CORS_ALLOW_HEADERS'] = ['Content-Type', 'Access-Control-Allow-Private-Network', 'Access-Control-Request-Private-Network']
toptext.config['CORS_METHODS'] = ['PUT', 'GET', 'REMOVE', 'PATCH']
toptext.config['CORS_HEADERS'] = 'Access-Control-Allow-Origin: *'

# toptext.config['CORS_HEADERS'] = 'Access-Control-Allow-Origin: https://aidenhuynh.github.io/leuckblewup'

# attention gamers, run the following command in terminal
# pip install Flask-Cors