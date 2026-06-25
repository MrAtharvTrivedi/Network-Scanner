## Network-Scanner

A Python-based network reconnaissance tool built for educational purposes 
and security auditing. It performs ARP-based host discovery to identify 
live hosts on a network, retrieves MAC addresses with vendor information, 
and conducts port scanning with service and banner detection.

### Features
- ARP scanning to discover live hosts on a network
- MAC address vendor lookup via macvendors.com API
- TCP port scanning with service identification
- Banner grabbing for open ports
- Support for single IP and CIDR range (e.g. 10.0.2.0/24)
- Modular design across multiple files

### Usage
# Network scan only
sudo python3 main.py -t 192.168.1.0/24

# Network scan + default port scan (1-1025)
sudo python3 main.py -t 192.168.1.0/24 --scan-ports

# Network scan + custom port range
sudo python3 main.py -t 192.168.1.0/24 -p 1-500

### Requirements
pip install scapy requests IPy

### Disclaimer
This tool is intended for educational purposes and authorized 
network testing only. Do not use on networks you don't own or 
have explicit permission to test.
