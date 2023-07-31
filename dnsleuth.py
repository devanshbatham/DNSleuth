#!/usr/bin/env python3


from scapy.all import *
from datetime import datetime
import colorama
import random

# Initialize colorama
colorama.init()

# Dictionary to store colors for each unique domain name and DNS record type
colors = {}

def get_color(key):
    """
    Returns a color for the given key, generating a new color if necessary.
    
    Parameters:
        key (str): The key to retrieve the color for.
        
    Returns:
        str: The color for the given key.
    """
    if key not in colors:
        # Use a random color for each unique key (excluding black)
        color = "\033[38;5;%dm" % (random.randint(1, 254))
        colors[key] = color
    return colors[key]

def dns_sniffer(pkt):
    """
    Sniffs DNS packets and prints the DNS queries with colors based on the domain name and DNS record type.
    
    Parameters:
        pkt (scapy.packet.Packet): The DNS packet to process.
    """
    if pkt.haslayer(DNS) and pkt[DNS].qr == 0:
        timestamp = datetime.fromtimestamp(pkt.time).strftime('%Y-%m-%d %H:%M:%S')
        query_type = pkt[DNSQR].qtype
        query_name = pkt[DNSQR].qname.decode()
        query_type_str = dnsqtypes.get(query_type, f"Unknown ({query_type})")
        
        # Get color for domain name and DNS record type
        name_color = get_color(query_name)
        type_color = get_color(query_type_str)
        date_color = "\033[36m" # Cyan
        
        # Print the output with the chosen colors
        print(f"[{date_color}{timestamp}{colorama.Style.RESET_ALL}] {name_color}{type_color}{query_type_str:<10} {query_name}{colorama.Style.RESET_ALL}")

try:
    # Sniff DNS packets on all interfaces
    sniff(filter="udp port 53", prn=dns_sniffer)
except KeyboardInterrupt:
    print("Sniffing stopped by user.")