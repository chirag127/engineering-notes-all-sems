## Experiment 4 - Write a code simulating PING and TRACEROUTE commands

- Ping and traceroute are common commands you can use to troubleshoot network problems  .
- Ping is a simple command that can test the reachability of a device on the network by sending an ICMP echo request and waiting for an ICMP echo reply   .
- Traceroute is a command you use to 'trace' the route that a packet takes when traveling to its destination by sending a series of ICMP echo requests with increasing TTL values and recording the ICMP time exceeded responses from the intermediate routers    .
- To write a code simulating ping and traceroute commands, you need to use a programming language that can send and receive raw network packets, such as Python, C, or Java.
- You also need to use a library or a module that can handle ICMP messages, such as scapy for Python, libnet for C, or jpcap for Java.
- The basic steps for writing a code simulating ping and traceroute commands are:

  - Import the necessary libraries or modules for network programming and ICMP handling.
  - Define a function for sending an ICMP echo request to a given destination address and port number, and returning the ICMP echo reply or an error message if any.
  - Define a function for sending a series of ICMP echo requests to a given destination address and port number, with increasing TTL values from 1 to a maximum limit, and returning the ICMP time exceeded responses or the ICMP echo reply from the destination if any.
  - Define a function for calculating the round-trip time (RTT) between sending and receiving an ICMP message, and formatting the output in a readable way.
  - Define a function for validating the user input, such as checking if the destination address is valid and reachable, and handling any exceptions or errors.
  - Define a main function for taking the user input, such as the destination address and port number, and the command to execute (ping or traceroute), and calling the appropriate functions to perform the network test and display the results.
  - Run the main function and test the code with different destination addresses and port numbers, and compare the results with the actual ping and traceroute commands.

- The following is an example of a code simulating ping and traceroute commands in Python, using the scapy module:

```python
# Import the scapy module
from scapy.all import *

# Define a function for sending an ICMP echo request and returning the ICMP echo reply or an error message
def send_ping(dst, port):
  # Create an ICMP echo request packet with the destination address and port number
  packet = IP(dst=dst)/ICMP()/UDP(dport=port)
  # Send the packet and wait for a response, with a timeout of 2 seconds
  response = sr1(packet, timeout=2, verbose=0)
  # If there is a response, return it
  if response:
    return response
  # If there is no response, return an error message
  else:
    return "Request timed out"

# Define a function for sending a series of ICMP echo requests with increasing TTL values and returning the ICMP time exceeded responses or the ICMP echo reply
def send_traceroute(dst, port):
  # Initialize an empty list for storing the responses
  responses = []
  # Initialize the TTL value to 1
  ttl = 1
  # Initialize a flag to indicate if the destination is reached
  reached = False
  # Loop until the destination is reached or the TTL value exceeds the maximum limit of 30
  while not reached and ttl <= 30:
    # Create an ICMP echo request packet with the destination address, port number, and TTL value
    packet = IP(dst=dst, ttl=ttl)/ICMP()/UDP(dport=port)
    # Send the packet and wait for a response, with a timeout of 2 seconds
    response = sr1(packet, timeout=2, verbose=0)
    # If there is a response, append it to the list of responses
    if response:
      responses.append(response)
      # If the response is an ICMP echo reply, set the flag to True and break the loop
      if response[ICMP].type == 0:
        reached = True
        break
    # If there is no response,