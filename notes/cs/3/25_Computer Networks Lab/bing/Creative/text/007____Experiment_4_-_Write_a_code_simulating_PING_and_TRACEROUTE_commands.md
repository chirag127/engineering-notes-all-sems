## Experiment 4 - Write a code simulating PING and TRACEROUTE commands

- PING and TRACEROUTE are two network diagnostic tools that can be used to test the connectivity and latency between two hosts on a network.
- PING sends a series of packets to a destination host and measures the time it takes for each packet to be echoed back. It also reports the packet loss rate and the round-trip time (RTT) statistics.
- TRACEROUTE traces the route that packets take from the source host to the destination host. It sends packets with increasing time-to-live (TTL) values and records the IP addresses of the routers that send back time-exceeded messages. It also measures the RTT for each hop along the path.
- To write a code simulating PING and TRACEROUTE commands, we need to use the socket module in Python, which provides low-level access to network interfaces. We also need to use the struct module to pack and unpack binary data, and the time module to measure the elapsed time.
- The following steps outline the basic algorithm for the code:

  - Create a raw socket with the ICMP protocol (Internet Control Message Protocol), which is used to send and receive error and control messages on the network.
  - Generate a unique identifier and a sequence number for each packet. The identifier and sequence number are used to match the echo request and echo reply packets.
  - Construct the ICMP header with the type, code, checksum, identifier, and sequence number fields. The type and code fields indicate the type of message, such as echo request or echo reply. The checksum field is used to verify the integrity of the packet. The identifier and sequence number fields are the same as the ones generated earlier.
  - Construct the ICMP payload with some arbitrary data. The payload can be any data, but it is usually a timestamp or a sequence of bytes.
  - Calculate the checksum of the ICMP header and payload and insert it into the header.
  - Pack the ICMP header and payload into a binary format using the struct module.
  - Send the packet to the destination host using the socket.sendto() method. Record the current time as the send time.
  - Wait for a response from the destination host using the socket.recvfrom() method. Record the current time as the receive time. If no response is received within a timeout period, report a timeout error and exit.
  - Unpack the response packet into the IP header and the ICMP header and payload using the struct module.
  - Check the type, code, identifier, and sequence number fields of the ICMP header to verify that it is a valid echo reply packet. If not, report an invalid packet error and exit.
  - Calculate the RTT by subtracting the send time from the receive time. Report the RTT, the packet size, and the destination IP address.
  - Repeat the above steps for a specified number of packets or until the user interrupts the program. Report the summary statistics, such as the minimum, maximum, average, and standard deviation of the RTT, and the packet loss rate.

- The following steps outline the basic algorithm for the TRACEROUTE code:

  - Create a raw socket with the ICMP protocol and another raw socket with the UDP protocol (User Datagram Protocol), which is used to send and receive datagrams on the network.
  - Generate a unique identifier and a sequence number for each packet. The identifier and sequence number are used to match the UDP datagram and the ICMP time-exceeded message.
  - Construct the UDP header with the source port, destination port, length, and checksum fields. The source port and destination port fields indicate the endpoints of the communication. The length field indicates the size of the UDP header and payload. The checksum field is used to verify the integrity of the packet. The source port can be any unused port, and the destination port can be any port that is unlikely to be open on the destination host, such as 33434.
  - Construct the UDP payload with some arbitrary data. The payload can be any data, but it is usually a timestamp or a sequence of bytes.
  - Calculate the checksum of the UDP header and payload and insert it into the header.
  - Pack the UDP header and payload into a binary format using the struct module.
  - Set the TTL value of the packet to 1 using the socket.setsockopt() method. The TTL value indicates how many hops the packet can traverse before being discarded by a router. By setting it to 1, we ensure that the packet will be discarded by the first router on the path and generate a time-exceeded message.
  - Send the packet to the destination host using the socket.sendto() method. Record the current time as the