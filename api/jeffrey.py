from flask import Flask, request, jsonify
import phonenumbers
import sqlite3
from phonenumbers import geocoder, timezone
import datetime

app = Flask(__name__)

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