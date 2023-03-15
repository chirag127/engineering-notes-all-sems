## Experiment 4 - Write a code simulating PING and TRACEROUTE commands

- PING and TRACEROUTE are common commands you can use to troubleshoot network problems  .
- PING is a simple command that can test the reachability of a device on the network by sending and receiving ICMP packets  .
- TRACEROUTE is a command you use to 'trace' the route that a packet takes when traveling to its destination by sending and receiving ICMP packets with varying TTL values   .
- To write a code simulating PING and TRACEROUTE commands, you need to follow these steps:

  - Import the necessary modules, such as socket, struct, time, sys, etc.
  - Define a function to calculate the checksum of an ICMP packet.
  - Define a function to create an ICMP packet with a given type, code, ID, sequence number, and payload.
  - Define a function to send an ICMP packet to a given destination address and port, and receive the response packet or timeout.
  - Define a function to perform the PING operation by sending and receiving ICMP packets with type 8 (echo request) and type 0 (echo reply), and printing the statistics such as RTT, packet loss, etc.
  - Define a function to perform the TRACEROUTE operation by sending and receiving ICMP packets with type 8 (echo request) and varying TTL values, and printing the intermediate hops and their RTT .
  - Use the main function to parse the command-line arguments and call the appropriate function based on the user input.

- Here is an example code in Python that simulates the PING and TRACEROUTE commands:

```python
# Import the necessary modules
import socket
import struct
import time
import sys

# Define a function to calculate the checksum of an ICMP packet
def checksum(data):
    # Initialize the sum to zero
    sum = 0
    # Loop through the data in 16-bit chunks
    for i in range(0, len(data), 2):
        # Add the 16-bit chunk to the sum
        if i + 1 < len(data):
            sum += (data[i] << 8) + data[i + 1]
        else:
            sum += data[i]
        # Add the carry bits to the sum
        sum = (sum & 0xffff) + (sum >> 16)
    # Return the one's complement of the sum
    return ~sum & 0xffff

# Define a function to create an ICMP packet with a given type, code, ID, sequence number, and payload
def create_packet(type, code, id, seq, payload):
    # Pack the header fields into a binary format
    header = struct.pack('!BBHHH', type, code, 0, id, seq)
    # Calculate the checksum of the header and payload
    chksum = checksum(header + payload)
    # Repack the header with the checksum
    header = struct.pack('!BBHHH', type, code, chksum, id, seq)
    # Return the header and payload as a packet
    return header + payload

# Define a function to send an ICMP packet to a given destination address and port, and receive the response packet or timeout
def send_packet(sock, dest_addr, port, packet, timeout):
    # Send the packet to the destination address and port
    sock.sendto(packet, (dest_addr, port))
    # Set the socket timeout
    sock.settimeout(timeout)
    # Try to receive the response packet
    try:
        response, addr = sock.recvfrom(1024)
        # Return the response packet and the address
        return response, addr
    # Handle the socket timeout exception
    except socket.timeout:
        # Return None and None
        return None, None

# Define a function to perform the PING operation by sending and receiving ICMP packets with type 8 (echo request) and type 0 (echo reply), and printing the statistics such as RTT, packet loss, etc
def ping(dest_addr, count, interval, timeout, payload_size):
    # Create a raw socket for ICMP protocol
    sock = socket.socket