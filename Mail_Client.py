#QUICK DISCLAIMER:
'''
this script allows you to send emails to spam a terget mail
DO NOT USE THIS SCRIPT TO CAUSE HARM!!
also use this script for education and learning somthing new. :)
'''
import pyfiglet # If you dont have this import type before run "pip/pip3 install pyfiglet"
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

#Banner for Program
banner = pyfiglet.figlet_format("CLIENT SPAMMER!!" ,width=110)
print(banner)
#Submit the Domain of you email
server = smtplib.SMTP('smtp.gmail.com', 25)

#Start the SMTP
server.ehlo()

#Cradentials For Email:
mail = input("Enter Your Email[NOTE: some domains not support this system]:\n")
password = input("Enter Your Password: ")

#Login to email
server.login(mail, password)

#Header of the email:
msg = MIMEMultipart()
msg['From'] = "Attacker!!"
Target_mail = msg['To'] = input("Enter a Mail Target: ")
msg['Subject'] = input("Enter a Subject: ")

#Contant of the mail:
Contant = input("Enter Contant Here:\n")
msg.attach(MIMEText(Contant, 'plain'))

#Send the mail
text = msg.as_string()
server.sendmail(mail, Target_mail, text)
