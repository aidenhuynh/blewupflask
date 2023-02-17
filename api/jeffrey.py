from flask import Flask, render_template, request, jsonify
import sqlite3
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_id = request.form['user_id']
    phone_number = request.form['phone_number']

    givenPN = phonenumbers.parse(phone_number, "CH")
    # get location
    ch_number = phonenumbers.parse(phone_number, "CH")
    location = geocoder.description_for_number(ch_number, "en")

    # get timezone
    timezoneOfPN = timezone.time_zones_for_number(givenPN)

    # get current time
    now = datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M:%S")

    ch_number = phonenumbers.parse(phone_number, "CH")
    location = geocoder.description_for_number(ch_number, "en")
    givenPN = phonenumbers.parse(phone_number, "CH")
    timezoneOfPN = timezone.time_zones_for_number(givenPN)
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    timezone1 = timezoneOfPN[0] if len(timezoneOfPN) > 0 else ""

    # connect to database
    conn = sqlite3.connect('api/sqlites.db')
    c = conn.cursor()
    c.execute("INSERT INTO phone VALUES (?, ?, ?, ?, ?)", (user_id, phone_number, location, timezone1, time))
    conn.commit()
    conn.close()

    return 'Data added to database'

@app.route('/api/phone')
def get_phone_data():
    conn = sqlite3.connect('api/sqlites.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM phone")
    data = cursor.fetchall()
    conn.close()

    results = []
    for row in data:
        result = {
            'user_id': row[0],
            'phone_number': row[1],
            'location': row[2],
            'timezone': row[3],
            'time': row[4]
        }
        results.append(result)

    return jsonify(results)

if __name__ == '__main__':
    app.run()