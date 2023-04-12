## Experiment 4 - Write a code simulating PING and TRACEROUTE commands

- PING and TRACEROUTE are two common network diagnostic tools that can test the connectivity and latency between two hosts on a network.
- PING sends a series of packets to a destination host and measures the time it takes for each packet to be sent and received. It also reports the number of packets lost or dropped during the transmission.
- TRACEROUTE sends a series of packets with increasing TTL (time to live) values and records the IP addresses of the routers that forward the packets along the path to the destination host. It also measures the round-trip time for each packet.
- To write a code simulating PING and TRACEROUTE commands, we need to use the socket module in Python, which provides low-level access to network interfaces and protocols.
- We also need to use the struct module, which allows us to pack and unpack binary data, and the time module, which provides various functions to manipulate time values.
- The following is a possible code for simulating PING and TRACEROUTE commands in Python:

```python
# Import the modules
import socket
import struct
import time

# Define some constants
ICMP_ECHO_REQUEST = 8 # ICMP type code for echo request packets
ICMP_ECHO_REPLY = 0 # ICMP type code for echo reply packets
ICMP_TIME_EXCEEDED = 11 # ICMP type code for time exceeded packets
MAX_HOPS = 30 # Maximum number of hops to trace the route
TIMEOUT = 2 # Timeout in seconds for each packet
PACKET_SIZE = 64 # Size of the ICMP packet in bytes

# Define a function to calculate the checksum of a packet
def checksum(packet):
    # Initialize the sum to zero
    sum = 0
    # Loop through every 16-bit word in the packet
    for i in range(0, len(packet), 2):
        # Add the 16-bit word to the sum
        sum += (packet[i] << 8) + packet[i+1]
    # Add the carry bits to the sum
    sum = (sum >> 16) + (sum & 0xffff)
    # Invert the sum and return it as a 16-bit unsigned integer
    return ~sum & 0xffff

# Define a function to create an ICMP packet
def create_packet(id, seq, data):
    # Create the ICMP header with the given id, sequence number and checksum
    header = struct.pack("!BBHHH", ICMP_ECHO_REQUEST, 0, 0, id, seq)
    # Calculate the checksum of the header and data
    chksum = checksum(header + data)
    # Recreate the header with the correct checksum
    header = struct.pack("!BBHHH", ICMP_ECHO_REQUEST, 0, chksum, id, seq)
    # Return the header and data as the packet
    return header + data

# Define a function to parse an ICMP packet
def parse_packet(packet):
    # Extract the ICMP header from the packet
    header = packet[20:28]
    # Unpack the header and get the type, code, checksum, id and sequence number
    type, code, chksum, id, seq = struct.unpack("!BBHHH", header)
    # Return the type, code, id and sequence number as a tuple
    return type, code, id, seq

# Define a function to simulate the PING command
def ping(dest_addr):
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_ICMP)
    # Set the socket timeout
    sock.settimeout(TIMEOUT)
    # Get the destination IP address
    dest_ip = socket.gethostbyname(dest_addr)
    # Print the ping message
    print(f"PING {dest_addr} ({dest_ip}) {PACKET_SIZE} bytes of data.")
    # Initialize the packet id, sequence number and data
    id = 0
    seq = 0
    data = b"\x00" * (PACKET_SIZE - 8)
    # Initialize the statistics variables
    sent = 0
    received = 0
    min_rtt = float("inf")
    max_rtt = 0
    total_rtt = 0
    # Loop for 10 packets
    for i in range(10):
        # Increment the packet id and sequence number
        id = (id + 1) & 0xffff
        seq = (seq + 1) & 0xffff
        # Create the packet

```
