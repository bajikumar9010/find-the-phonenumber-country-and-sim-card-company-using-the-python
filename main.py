import phonenumbers
from phonenumbers import geocoder

# Parse phone number
phone_number = phonenumbers.parse("+91 give your phnumber", "IND")

# Get location information
location = geocoder.description_for_number(phone_number, "en")
print(location)
from phonenumbers import carrier
service_number=phonenumbers.parse("+91give your number","RO")
print(carrier.name_for_number(service_number,"en"))


