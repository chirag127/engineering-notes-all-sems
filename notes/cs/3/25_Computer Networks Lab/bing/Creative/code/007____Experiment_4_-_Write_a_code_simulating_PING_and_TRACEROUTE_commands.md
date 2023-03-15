## Experiment 4 - Write a code simulating PING and TRACEROUTE commands

- PING and TRACEROUTE are common commands you can use to troubleshoot network problems  .
- PING is a simple command that can test the reachability of a device on the network by sending and receiving ICMP packets   .
- TRACEROUTE is a command you use to 'trace' the route that a packet takes when traveling to its destination by sending and receiving ICMP packets with varying TTL values   .
- To write a code simulating PING and TRACEROUTE commands, you need to follow these steps:

  1. Import the necessary modules, such as socket, struct, time, sys, etc.
  2. Define a function to calculate the checksum of an ICMP packet, which is used to verify the integrity of the packet .
  3. Define a function to create an ICMP packet, which consists of a header and a payload . The header contains the type, code, checksum, identifier, and sequence number fields. The payload contains the timestamp and some arbitrary data.
  4. Define a function to send an ICMP packet to a given destination address and port, and receive the response packet from the same address and port . The function should also measure the round-trip time (RTT) of the packet and return it along with the response packet.
  5. Define a function to perform the PING operation, which takes a destination address and a number of packets as arguments . The function should loop through the number of packets, call the send and receive function for each packet, and print the RTT and the response packet information. The function should also calculate and print the statistics of the PING operation, such as the number of packets transmitted, received, lost, and the minimum, maximum, and average RTT.
  6. Define a function to perform the TRACEROUTE operation, which takes a destination address as an argument . The function should loop through the TTL values from 1 to 30, call the send and receive function for each TTL value, and print the RTT and the response packet information. The function should also check the type and code fields of the response packet to determine if the destination is reached or not. The function should stop the loop if the destination is reached or the maximum TTL value is reached.
  7. Write the main code to parse the command-line arguments, such as the destination address and the number of packets, and call the appropriate function based on the command (PING or TRACEROUTE).
  8. Run the code and test the output with different destination addresses and compare the results with the actual PING and TRACEROUTE commands.

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
def create_packet(identifier, sequence_number):
  # Define the ICMP type and code for echo request
  icmp_type = 8
  icmp_code = 0
  # Initialize the checksum to zero
  checksum = 0
  # Pack the header fields into a binary format
  header = struct.pack('!BBHHH', icmp_type, icmp_code, checksum, identifier, sequence_number)
  # Get the current timestamp in milliseconds
  timestamp = int(time.time() * 1000)
  # Pack the