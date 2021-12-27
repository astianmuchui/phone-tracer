import phonenumbers

number = "+4775497946779464" #Add number here

from phonenumbers import geocoder

ch_nmber = phonenumbers.parse(number,"CH")

print(geocoder.description_for_number(ch_nmber,"en"))

from phonenumbers import carrier

service = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service,"en"))
