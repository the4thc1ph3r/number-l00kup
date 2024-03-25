import phonenumbers
from phonenumbers import geocoder

from termcolor import colored
text = colored('--------------number-l00kup by the4thc1ph3r--------------', 'green', attrs=['blink'])
print(text)

number = input("Enter the phone number(+91xxxxxxxxx): ")

country = phonenumbers.parse(number, "CH")
print("The number is from: ", geocoder.description_for_number(country, "en"))

from phonenumbers import carrier

service = phonenumbers.parse(number, "RO")

print("The service provider is: ", carrier.name_for_number(service, "en"))
