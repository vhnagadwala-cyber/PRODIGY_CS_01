# Task 05 - Network Packet Analyzer
# Prodigy InfoTech Cyber Security Internship
# Author: Veer Nagadwala
#
# Every time you open a website, send a message, or load a video,
# your computer is sending and receiving tiny chunks of data called "packets".
# A packet analyzer (also called a sniffer) lets us see these packets in real time.
#
# This is a core tool in cybersecurity - used by professionals to monitor
# networks, spot suspicious activity, and troubleshoot issues.
#
# ⚠️ Only use this on your own network or with permission.
#    Sniffing someone else's traffic without consent is illegal.
#
# Install requirement: pip install scapy
# Run as administrator (Windows) or sudo (Linux/Mac)

from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw
from datetime import datetime

LOG_FILE = "packet_log.txt"
PACKET_LIMIT = 50  # How many packets to capture (set to 0 for unlimited)

packet_count = 0


def protocol_name(num):
    # Common protocol numbers and their names
    names = {1: "ICMP", 6: "TCP", 17: "UDP"}
    return names.get(num, f"Unknown ({num})")


def show_packet(packet):
    global packet_count
    packet_count += 1

    time_now = datetime.now().strftime("%H:%M:%S")
    lines = []
    lines.append(f"\n{'─'*52}")
    lines.append(f"  Packet #{packet_count}   |   Captured at {time_now}")
    lines.append(f"{'─'*52}")

    # Show basic IP info
    if IP in packet:
        ip = packet[IP]
        lines.append(f"  From       :  {ip.src}")
        lines.append(f"  To         :  {ip.dst}")
        lines.append(f"  Protocol   :  {protocol_name(ip.proto)}")
        lines.append(f"  TTL        :  {ip.ttl}")

    # Extra TCP details (most web traffic uses TCP)
    if TCP in packet:
        tcp = packet[TCP]
        flags = []
        if tcp.flags & 0x02: flags.append("SYN")
        if tcp.flags & 0x10: flags.append("ACK")
        if tcp.flags & 0x01: flags.append("FIN")
        if tcp.flags & 0x04: flags.append("RST")
        if tcp.flags & 0x08: flags.append("PSH")
        lines.append(f"  From Port  :  {tcp.sport}")
        lines.append(f"  To Port    :  {tcp.dport}")
        lines.append(f"  TCP Flags  :  {', '.join(flags) if flags else 'None'}")

    # UDP details (used by DNS, games, video calls etc.)
    if UDP in packet:
        udp = packet[UDP]
        lines.append(f"  From Port  :  {udp.sport}")
        lines.append(f"  To Port    :  {udp.dport}")

    # ICMP is used for ping
    if ICMP in packet:
        icmp = packet[ICMP]
        lines.append(f"  ICMP Type  :  {icmp.type}")
        lines.append(f"  ICMP Code  :  {icmp.code}")

    # Show a small preview of the data inside the packet
    if Raw in packet:
        raw = packet[Raw].load
        try:
            preview = raw.decode("utf-8", errors="replace")[:80].replace("\n", " ")
            lines.append(f"  Data       :  {preview}...")
        except Exception:
            lines.append(f"  Data       :  [binary, {len(raw)} bytes]")

    output = "\n".join(lines)
    print(output)

    # Save to log file too
    with open(LOG_FILE, "a") as f:
        f.write(output + "\n")


def main():
    print("\n======================================")
    print("   Network Packet Analyzer")
    print("   Prodigy InfoTech | Task 05")
    print("======================================")
    print("\n⚠️  For educational use only - use on your own network!")
    print(f"\nCapturing up to {PACKET_LIMIT} packets... (0 = unlimited)")
    print(f"Saving log to: {LOG_FILE}")
    print("Press CTRL+C to stop anytime.\n")

    try:
        sniff(
            prn=show_packet,
            count=PACKET_LIMIT,
            store=False,
            filter="ip"
        )
    except KeyboardInterrupt:
        print("\nCapture stopped by user.")
    except PermissionError:
        print("\nPermission denied! Please run this script as administrator or with sudo.")

    print(f"\nTotal packets captured: {packet_count}")
    print(f"Full log saved in: {LOG_FILE}")


if __name__ == "__main__":
    main()
