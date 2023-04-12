## Experiment 4 - Write a code simulating PING and TRACEROUTE commands

- PING and TRACEROUTE are common commands you can use to troubleshoot network problems  .
- PING is a simple command that can test the reachability of a device on the network by sending and receiving ICMP packets   .
- TRACEROUTE is a command you use to 'trace' the route that a packet takes when traveling to its destination by sending and receiving ICMP packets with varying TTL values    .
- To write a code simulating PING and TRACEROUTE commands, you need to follow these steps:

  - Import the necessary modules, such as socket, struct, time, sys, etc.
  - Define a function to calculate the checksum of an ICMP packet, which is used to verify the integrity of the packet .
  - Define a function to create an ICMP packet, which consists of a header and a payload. The header contains the type, code, checksum, identifier, and sequence number fields. The payload contains the timestamp and some arbitrary data .
  - Define a function to send an ICMP packet to a given destination address and port, using a raw socket. The function should also receive the ICMP reply packet and calculate the round-trip time (RTT) and the hop count .
  - Define a function to perform the PING operation, which involves sending and receiving multiple ICMP packets to a given destination and displaying the statistics, such as the number of packets sent, received, lost, the minimum, maximum, and average RTT, etc   .
  - Define a function to perform the TRACEROUTE operation, which involves sending and receiving ICMP packets with increasing TTL values, starting from 1, to a given destination and displaying the intermediate routers and their RTTs    .
  - Write the main code to take the user input for the destination address and the operation (PING or TRACEROUTE) and call the corresponding function to execute it.

- Here is an example of a code simulating PING and TRACEROUTE commands in Python:

```python
# Import the necessary modules
import socket
import struct
import time
import sys

# Define a function to calculate the checksum of an ICMP packet
def checksum(packet):
    # Initialize the sum to zero
    sum = 0
    # Loop through the packet in 16-bit chunks
    for i in range(0, len(packet), 2):
        # Add the 16-bit chunks to the sum
        sum += (packet[i] << 8) + packet[i+1]
    # Add the carry bits to the sum
    sum = (sum >> 16) + (sum & 0xffff)
    # Invert the sum and return it
    return ~sum & 0xffff

# Define a function to create an ICMP packet
def create_packet(id, seq, data):
    # Define the ICMP header fields
    type = 8 # Echo request
    code = 0 # No code
    checksum = 0 # Placeholder
    identifier = id # Identifier
    sequence = seq # Sequence number
    # Pack the header fields into a binary format
    header = struct.pack('!BBHHH', type, code, checksum, identifier, sequence)
    # Append the payload to the header
    packet = header + data
    # Calculate the checksum of the packet
    checksum = checksum(packet)
    # Repack the header with the checksum
    header = struct.pack('!BBHHH', type, code, checksum, identifier, sequence)
    # Return the packet
    return header + data

# Define a function to send and receive an ICMP packet
def send_packet(dest, port, id, seq, ttl, data):
    # Create a raw socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    # Set the socket timeout
    sock.settimeout(1)
    # Set the socket TTL
    sock

```
