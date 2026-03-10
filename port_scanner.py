import socket
import datetime

def scan_port(host, port, timeout=1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        if result == 0:
            return True
    except:
        pass
    return False

def get_service(port):
    common = {
        21: "FTP", 22: "SSH", 23: "Telnet",
        25: "SMTP", 53: "DNS", 80: "HTTP",
        110: "POP3", 143: "IMAP", 443: "HTTPS",
        3306: "MySQL", 3389: "RDP", 5432: "PostgreSQL",
        6379: "Redis", 8080: "HTTP-Alt", 8443: "HTTPS-Alt"
    }
    return common.get(port, "Unknown")

def scan_host(host, start_port, end_port):
    print("=" * 50)
    print(f"  🔍 Port Scanner by Kanthi Phoosorn")
    print("=" * 50)
    print(f"🎯 Target: {host}")
    print(f"📡 Range:  {start_port} - {end_port}")
    print(f"⏰ Start:  {datetime.datetime.now().strftime('%H:%M:%S')}")
    print("=" * 50)

    open_ports = []

    for port in range(start_port, end_port + 1):
        if scan_port(host, port):
            service = get_service(port)
            open_ports.append(port)
            print(f"✅ Port {port:5d} OPEN  — {service}")

    print("=" * 50)
    print(f"✅ Scan complete — {len(open_ports)} open ports found")
    print(f"⏰ End: {datetime.datetime.now().strftime('%H:%M:%S')}")
    print("=" * 50)

def main():
    print("\n🔐 Port Scanner — Kanthi Phoosorn\n")
    host = input("Enter target IP or hostname: ")
    start = int(input("Start port: "))
    end = int(input("End port: "))
    scan_host(host, start, end)

main()
