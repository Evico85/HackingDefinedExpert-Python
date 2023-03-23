'''
==============================================================================================================================================================
This is a script for scanning Target IP's and Hashes to check if they malicious by go to virustotal or AbuseIPDB and check them there and give you results.
IMPORTANT NOTE : you need API_KEY from VirusTotal in order the script to work.
i put inside the code the places where you need to put your API_KEY in order the code to work.
==============================================================================================================================================================
'''
import pyfiglet
import hashlib
import requests
import json
import ipwhois

banner = pyfiglet.figlet_format("MALICIOUS SCANNER", font = "digital")
print(banner)
print("Welcome To my malicious scanner program!!")
def check_hash(hash):
    # Check if the hash is valid
    if len(hash) == 32 or len(hash) == 40 or len(hash) == 64:
        return True
    else:
        return False

def scan_hash(hash):
    # Scan the hash in VirusTotal
    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    params = {'apikey': 'YOUR_API_KEY', 'resource': hash}
    response = requests.get(url, params=params)
    json_response = response.json()
    if json_response['response_code'] == 0:
        print('The hash is not detected by any antivirus engines.')
    else:
        print('The hash is malicious according to the following antivirus engines:')
        for engine in json_response['scans']:
            if json_response['scans'][engine]['detected'] == True:
                print(engine)

def check_ip(ip_address):
    # Check if the IP address is valid
    try:
        ipwhois.IPWhois(ip_address).lookup_rdap()
        return True
    except ipwhois.exceptions.IPDefinedError:
        return False

def scan_ip_vt(ip_address):
    # Scan the IP address in VirusTotal
    url = 'https://www.virustotal.com/vtapi/v2/ip-address/report'
    params = {'apikey': 'YOUR_API_KEY', 'ip': ip_address}
    response = requests.get(url, params=params)
    json_response = response.json()
    if json_response['response_code'] == 0:
        print('The IP address is not detected as malicious in VirusTotal.')
    else:
        print('The IP address is malicious according to the following categories in VirusTotal:')
        for category in json_response['categories']:
            print(category)

def scan_ip_ab(ip_address):
    # Scan the IP address in AbuseIPDB
    url = f'https://api.abuseipdb.com/api/v2/check?ipAddress={ip_address}'
    headers = {'Key': 'YOUR_API_KEY', 'Accept': 'application/json'}
    response = requests.get(url, headers=headers)
    json_response = response.json()
    if json_response['data']['abuseConfidenceScore'] > 0:
        print('The IP address is malicious according to the following categories in AbuseIPDB:')
        for category in json_response['data']['categories']:
            print(category['name'])
    else:
        print('The IP address is not detected as malicious in AbuseIPDB.')

# Main code
scan_ip = input('Do you want to scan an IP address? (y/n) ')
if scan_ip.lower() == 'y':
    ip_address = input('Enter the IP address to scan: ')
    if check_ip(ip_address):
        scan_ip_vt(ip_address)
        scan_ip_ab(ip_address)
    else:
        print('The IP address is not valid.')
else:
    hash = input('Enter the hash to scan: ')
    if check_hash(hash):
        scan_hash(hash)
    else:
        print('The hash is not valid.')
