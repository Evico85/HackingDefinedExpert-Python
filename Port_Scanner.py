#QUICK DISCLAIMER:
'''
this script allows you to scan target IP for Potential open Ports
DONT USE THIS SCRIPT TO CAUSE HARM
This code is meants for educational purposess only.
'''
import queue
import socket
import threading
from queue import Queue
import pyfiglet # If you dont have this import type before run "pip/pip3 install pyfiglet"

#Banner
banner = pyfiglet.figlet_format("PORT SCANNER!!" ,width=110)
print(banner)

#Enter Target To Scan
target = input("Enter IP target: ")

queue = Queue()
open_ports = []

#Function For Scaning:
def port_scan(port):
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect((target,port))
        return True
    except:
        return False
#Prevent from scanning the same port twice:
def fill_queue(port_list):
    for port in port_list:
        queue.put(port)       
#Check if port is open and add it to list of open ports:        
def worker():
    while not queue.empty():
        port = queue.get()
        if port_scan(port):
            print("Port {} is open!".format(port))
            open_ports.append(port)   
#Range of port to scan:
end_port_to_scan = int(input("Enter the range you want to scan\n[For Example for range 1-10 put number 10]\nYour Choose?: "))
print("Scaning...")
port_list = range(1, end_port_to_scan)
fill_queue(port_list)

thread_list = []

for t in range(500):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()
    
print("Open ports are: ",open_ports)