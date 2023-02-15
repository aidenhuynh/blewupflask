from flask import Flask

import phonenumbers
import sqlite3
from text import number
from text import user_id
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone  

print("User_ID:", user_id + "\n")
print("Inputted Phone Number:", number + "\n")

ch_number = phonenumbers.parse(number, "CH")
print("Current Location:", geocoder.description_for_number(ch_number, "en") + "\n")

givenPN = phonenumbers.parse(number, "CH")  
# Using parse phone number for finding timezone  
timezoneOfPN = timezone.time_zones_for_number(givenPN)  
# Printing carrier as the result  
print("The timezone of the given phone number is:", timezoneOfPN, "\n") 

import datetime
now = datetime.datetime.now()
print ("The current date and time is:", now.strftime("%Y-%m-%d %H:%M:%S"))

location = geocoder.description_for_number(ch_number, "en")
timezone1 = timezoneOfPN
time = now.strftime("%Y-%m-%d %H:%M:%S")








def insertVaribleIntoTable(user_id, number, location, timezone1, time):
    try:
        sqliteConnection = sqlite3.connect('sqlites.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_with_param = """INSERT INTO phone
                          (user_id, phone_number, location, timezone, time) 
                          VALUES (?, ?, ?, ?, ?);"""

        data_tuple = (user_id, number, location, timezone1, time)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("Values inserted successfully into the 'phone' table")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert values into the 'phone' table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
            
insertVaribleIntoTable(1, '123456789', 'Seattle', 'PST', '2022-01-01 10:00:00')