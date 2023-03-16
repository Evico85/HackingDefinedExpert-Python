#QUICK DISCLAIMER:
'''
this script allows you to see a mobile number information by typing only the user phone number
DO NOT USE THIS SCRIPT TO CAUSE HARM!!
also you check it out on your mobile device and see if its work to learn something new :)
'''
import phonenumbers # If you dont have this import type before run "pip/pip3 install phonenumbers"
from phonenumbers import carrier, geocoder, timezone
import pyfiglet  # If you dont have this import type before run "pip/pip3 install pyfiglet"

#Banner
banner = pyfiglet.figlet_format("PHONE INFO" ,width=110)
print(banner)

#Enter Mobile number for Checking..
Mobile_Number = input("Enter Mobile number with country code: ")
Mobile_Number = phonenumbers.parse(Mobile_Number)


#Print results after check
print("The Location of the phone is in:",timezone.time_zones_for_number(Mobile_Number))
print("The name of Service Provider:",carrier.name_for_number(Mobile_Number,"en"))
print("The Location Country:",geocoder.description_for_number(Mobile_Number,"en"))
print("Valid Mobile Number:",phonenumbers.is_valid_number(Mobile_Number))
print("Checking possibility of Number:",phonenumbers.is_possible_number(Mobile_Number))
