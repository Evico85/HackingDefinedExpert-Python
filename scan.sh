=============================================================================================================
#This is a script for scanning Targets for open ports and checks if its a webserver and if its is the script
#will scan the webserver for potential exploits.
# DO NOT RUN THIS SCRIPT WITHOUT PREMISSION
==============================================================================================================
#!/bin/bash

# Ask for target IP address
read -p "Enter target IP address: " ip

# Validate IP address
if ! [[ $ip =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
  echo "Invalid IP address"
  exit 1
fi

# Ask for scan type
read -p "Perform regular scan (r) or aggressive scan (a)? " scan_type

# Regular scan
if [[ $scan_type = "r" ]]; then
  echo "Performing regular scan on $ip"
  nmap -sC -sV -oN "Nmap scan for $ip" -Pn $ip
# Aggressive scan
elif [[ $scan_type = "a" ]]; then
  echo "Performing aggressive scan on $ip"
  nmap -A -T4 -p- -oN "Nmap aggressive_scan for $ip" $ip
else
  echo "Invalid scan type"
  exit 1
fi

# Check for webserver and prompt for GoBuster
echo "Checking for webserver.."
webserver_ports=$(nmap -p 80,443 --open $ip | grep "open" | cut -d'/' -f1)

if [[ ! -z $webserver_ports ]]; then
  read -p "Found webserver on port $webserver_ports, do you want to run GoBuster on that port? (y/n) " run_gobuster
  if [[ $run_gobuster = "y" ]]; then
    gobuster dir -u http://$ip:$webserver_ports -w /usr/share/wordlists/dirb/common.txt -o "GoBuster Results"
    echo "Running fuff on http://$ip:$webserver_ports"
    fuff -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt -u http://$ip:$webserver_ports/FUZZ -fs 424242 -o "fuff_Results"
    read -p "Do you want to scan for potential XSS or CSRF on http://$ip:$webserver_ports? (y/n) " scan_xss_csrf
    if [[ $scan_xss_csrf = "y" ]]; then
      echo "Scanning for potential XSS or CSRF on http://$ip:$webserver_ports"
      xsser -u http://$ip:$webserver_ports -c -g -v -o "XSS_and_CSRF_Potential"
    fi
  fi
fi
