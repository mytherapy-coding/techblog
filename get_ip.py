import socket

def get_all_ip_addresses(domain_name):
    try:
        _, _, ip_addresses = socket.gethostbyname_ex(domain_name)
        print(f"All IP addresses for {domain_name}: {', '.join(ip_addresses)}")
    except socket.gaierror:
        print(f"Unable to get IP addresses for {domain_name}")


domain_name = "google.com"
get_all_ip_addresses(domain_name)

