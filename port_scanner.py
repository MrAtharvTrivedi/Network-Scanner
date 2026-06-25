import socket

class Portscanner:
    def __init__(self, ip, port_range="1-1025"):
        self.ip = ip

        if "-" in port_range:
            self.start_port, self.end_port = map(int, port_range.split("-"))
        else:
            self.start_port = int(port_range)
            self.end_port = int(port_range) + 1
    

    def get_banner(self, s):
        try:
            return s.recv(1024)
        except:
            return b"No banner"

    def scan_port(self, ip, port):
        try:
            connection = socket.socket()
            connection.settimeout(2)
            connection.connect((ip, port))
            banner = self.get_banner(connection)
            connection.close()

            try:
                service = socket.getservbyport(port)
            except:
                service = "unknown"
                
            try:
                print(f"{port}\t\topen\t\t{service}\t\t{banner.decode().strip()}")
            except UnicodeDecodeError:
                print(f"{port}\t\topen\t\t{service}\t\t{str(banner)}")


        except (socket.timeout, ConnectionRefusedError, OSError):
            pass
            

    def run(self):

        if not self.ip:
            print("\n\n[-] No host is up at the moment")
            exit(1)

        for live_host in self.ip: 
            print(f"\n\nPort scan report for : {live_host}")

            print("---------------------------------------------------------------------------")
            print("Port\t\tState\t\tService\t\tBanner")
            print("---------------------------------------------------------------------------")

            for port in range(self.start_port, self.end_port):
                self.scan_port(live_host, port)
