import scapy.all as scapy
import requests
import time

class Netscanner:
    def __init__(self, ip):
        self.ip = ip
        self.live_hosts = []

    def get_mac_vendor(self, mac_address):
        
        try:
            time.sleep(.5)
            response = requests.get(f"https://api.macvendors.com/{mac_address}", timeout=3)
            return response.text

        except Exception as e:
            return "Unknown"

    def scan(self, ip):
        arp_request = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast/arp_request
        answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

        clients_list = []
        for element in answered_list:
            self.live_hosts.append(element[1].psrc)
            vendor_name = self.get_mac_vendor(element[1].hwsrc)
            client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc, "vendor": vendor_name}
            clients_list.append(client_dict)
        return clients_list

    def run(self):
        results_list = self.scan(self.ip)

        print("---------------------------------------------------------------------------")
        print("IP\t\t\tMAC Address\t\t\tVendor Name")
        print("---------------------------------------------------------------------------")

        for client in results_list:
            print(client["ip"] + "\t\t" + client["mac"] + "\t\t" + client["vendor"])

    def return_live_hosts(self):
        return self.live_hosts