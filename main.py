import scapy.all as scapy


def packet_callback(packet):
    print(packet.show()) 


def start_sniffing(interface="wlan0"):
    print(f"Sniffing packets on interface {interface}...")
    scapy.sniff(iface=interface, prn=packet_callback, store=0)  


if _name_ == "_main_":
    start_sniffing("wlan0")  
