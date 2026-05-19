import phonenumbers
from phonenumbers import PhoneNumberFormat, PhoneNumberType, geocoder, carrier, timezone
import geocoder

number = phonenumbers.parse('+359876699644')
geocode_data = data

print('Is valid number:', phonenumbers.is_valid_number(number))
print('International format:', phonenumbers.format_number(number, PhoneNumberFormat.INTERNATIONAL))
print('National format:', phonenumbers.format_number(number, PhoneNumberFormat.NATIONAL))

num_type = phonenumbers.number_type(number)

if num_type == PhoneNumberType.MOBILE:
    print('This is a mobile number')
else:
    print('This is a landline number')

print('Current Geocode Location:, geocode_data')
