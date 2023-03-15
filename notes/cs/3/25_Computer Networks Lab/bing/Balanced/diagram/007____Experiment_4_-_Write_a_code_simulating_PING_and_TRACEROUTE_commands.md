## Experiment 4 - Write a code simulating PING and TRACEROUTE commands

- PING and TRACEROUTE are common commands you can use to troubleshoot network problems .
- PING is a simple command that can test the reachability of a device on the network by sending and receiving ICMP packets   .
- TRACEROUTE is a command you use to 'trace' the route that a packet takes when traveling to its destination by sending and receiving ICMP packets with varying TTL values  .
- The code for simulating PING and TRACEROUTE commands can be written in Python using the socket and struct modules.
- The code should perform the following steps:
  - Import the socket and struct modules
  - Define a function to calculate the checksum of an ICMP packet
  - Define a function to create an ICMP echo request packet
  - Define a function to send and receive an ICMP packet using a socket
  - Define a function to perform a PING operation by sending and receiving one ICMP packet and measuring the round-trip time
  - Define a function to perform a TRACEROUTE operation by sending and receiving multiple ICMP packets with increasing TTL values and recording the intermediate hops
  - Define a main function to take the destination address as an argument and call the PING and TRACEROUTE functions
  - Run the main function with a sample destination address
- The code should handle any exceptions or errors that may occur during the socket operations
- The code should print the results of the PING and TRACEROUTE operations in a readable format
- The code should follow the Python coding style and conventions
- The code should be commented and documented
- The code should be tested and verified