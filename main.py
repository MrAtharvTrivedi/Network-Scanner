import argparse
import network_scanner as ns
import port_scanner as ps

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP / IP range")
    parser.add_argument("--scan-ports", dest="scan_ports", action="store_true", help="Scans Ports from 1 to 1025 ")
    parser.add_argument("-p", "--port-range", dest="ports", help="Target Port / Port Range") 
    options = parser.parse_args()
    return options.target, options.scan_ports, options.ports


target_ip, scan_ports, port_range =  get_arguments()


if not target_ip:
    print("[-] Please specify a target IP. Use -t <IP/range>")
    exit(1)

if scan_ports and port_range:
    print("[-] Use either --scan-ports (default range) or -p (custom range), not both.")
    exit(1)


print(f"\nTarget: {target_ip}\n")

my_network_scanner = ns.Netscanner(target_ip)  
my_network_scanner.run()


# Option 2 - port scan with default range
if scan_ports and not port_range:
    live_hosts = my_network_scanner.return_live_hosts()
    my_port_scanner = ps.Portscanner(live_hosts)
    my_port_scanner.run()

# Option 3 - port scan with custom range
if port_range:
    live_hosts = my_network_scanner.return_live_hosts()
    my_port_scanner = ps.Portscanner(live_hosts, port_range)
    my_port_scanner.run()

