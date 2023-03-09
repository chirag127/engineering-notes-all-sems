 Here is the content in markdown format:

## Experiment 4 - Write a code simulating PING and TRACEROUTE commands

PING and TRACEROUTE are two commonly used commands to diagnose network issues. Let us write a code to simulate the working of these commands:

1. PING:

- PING sends ICMP ECHO_REQUEST packets to a target host and waits for ICMP ECHO_REPLY packets.
- By calculating the time taken for the packets to be sent and reply received, the latency and packet loss can be calculated.
- A code can be written to send ping requests to a target IP address/host and display the response time and packet loss percentage.
- This can help in checking if a host is reachable and estimating the network latency.

2. TRACEROUTE:

- TRACEROUTE works by increasing the Time-To-Live field in the IP header and recording the source of the ICMP TIME_EXCEEDED replies.
- The TTL is incremented by 1 for each probe sent. This results in the probes getting replies from each successive router on the path to the destination.
- By recording the source IP address and latency of each reply, the route taken and latency at each router/link can be calculated.
- A code can be written to perform a traceroute to a destination IP and display the route path and latency at each hop.
- This can help in diagnosing where exactly a network latency or connectivity issue is occurring.

The code can be written in languages like Python or C and can make use of sockets and ICMP protocols to implement the PING and TRACEROUTE functionalities. The output can be displayed in a user-friendly format with details of the latency, loss, and route path. Such a code can be useful to learn and understand the working of these useful network troubleshooting commands.