import phonenumbers

from text import number
from phonenumbers import geocoder

ch_number = phonenumbers.parse(number, "CH")
print("Current Location:")
print(geocoder.description_for_number(ch_number, "en"))
print(" ")

import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))