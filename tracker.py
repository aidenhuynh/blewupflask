import phonenumbers

from text import number
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone  

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



