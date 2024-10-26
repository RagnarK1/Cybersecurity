import socket
import argparse

def validate_host(host):
    try:
        socket.gethostbyname(host)
        return True
    except socket.error:
        return False

def scan_port(host, port, protocol):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM if protocol == 'tcp' else socket.SOCK_DGRAM)
        sock.settimeout(1)  # Set timeout to 1 second
        if protocol == 'tcp':
            result = sock.connect_ex((host, port))
        else:
            sock.sendto(b'', (host, port))
            result = 0
        if result == 0:
            print(f"Port {port} is open")
            # If you want to show the service name using the port, you can do that here
        else:
            print(f"Port {port} is closed")
        sock.close()
    except socket.error as e:
        if protocol == 'udp':
            print(f"Error occurred while scanning port {port} using UDP: {e}")
        else:
            print("Error occurred while scanning port")

def main():
    parser = argparse.ArgumentParser(prog='tinyscanner', usage='%(prog)s [OPTIONS] [HOST] [PORT]', description='Simple port scanner')
    parser.add_argument('host', help='Target host IP address')
    parser.add_argument('-p', '--port', metavar='', help='Range of ports to scan')
    parser.add_argument('-t', '--tcp', action='store_true', help='Perform TCP scan')
    parser.add_argument('-u', '--udp', action='store_true', help='Perform UDP scan')

    args = parser.parse_args()

    if not validate_host(args.host):
        print("Invalid host or unable to resolve the hostname.")
        return

    protocol = 'tcp' if args.tcp else 'udp'

    if args.port:
        if '-' in args.port:
            start_port, end_port = map(int, args.port.split('-'))
            for port in range(start_port, end_port + 1):
                scan_port(args.host, port, protocol)
        else:
            scan_port(args.host, int(args.port), protocol)
    else:
        print("Port argument is required for single port scan.")

if __name__ == '__main__':
    main()
