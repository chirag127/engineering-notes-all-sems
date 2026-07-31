## Experiment 4 - Write a code simulating PING and TRACEROUTE commands

In this experiment, you will learn how to write a Python code to simulate the PING and TRACEROUTE commands.

### Introduction
- The PING command is used to test the connectivity between two network devices.
- The TRACEROUTE command is used to identify the path taken by a packet from the source to the destination.

### PING Command
- The PING command sends an ICMP echo request packet to the destination and waits for an ICMP echo reply packet.
- If the destination responds with an ICMP echo reply packet, the PING command reports that the packet was successfully transmitted and received.
- If the destination fails to respond with an ICMP echo reply packet, the PING command reports that the packet was lost.

### TRACEROUTE Command
- The TRACEROUTE command sends a series of ICMP echo request packets with increasing TTL values to the destination.
- Each router along the path decrements the TTL value of the packet and sends an ICMP time exceeded packet back to the source.
- The TRACEROUTE command reports the IP address of each router along the path.

### Writing the Code
- First, import the necessary modules: `socket`, `time`, and `struct`.
- For the PING command, create an ICMP echo request packet using the `struct` module.
- Send the ICMP echo request packet to the destination using a socket connection.
- Receive the ICMP echo reply packet from the destination using the socket connection.
- Calculate the round-trip time between the transmission and reception of the ICMP echo request and reply packets.
- For the TRACEROUTE command, create a series of ICMP echo request packets with increasing TTL values.
- Send each ICMP echo request packet to the destination using a socket connection.
- Receive the ICMP time exceeded packet from each router along the path using the socket connection.
- Extract the IP address of each router from the ICMP time exceeded packet and report it.

### Conclusion
In this experiment, you learned how to write a Python code to simulate the PING and TRACEROUTE commands. These commands are useful for testing network connectivity and identifying the path taken by a packet from the source to the destination. By understanding how these commands work and how to simulate them using Python, you can better troubleshoot network issues and improve network performance.