 Here is the content written in markdown format about UDP Transport layer protocol:

#### UDP Transport layer protocol

UDP or User Datagram Protocol is a transport layer protocol that provides fast but unreliable data transfer. It is a connectionless protocol as it does not establish a dedicated end-to-end connection between the source and destination.

Some key points about UDP:

- It is faster than TCP as it has less overhead. It does not establish a connection or ensure delivery of packets.
- Packets are sent as datagrams and are checked for errors only at the destination.
- It is preferred for applications that require fast transmission of data such as video streaming, online games, DNS etc. where some loss of packets is tolerable.
- The port numbers used by UDP are distinct from TCP port numbers. Well known UDP port numbers include 53 (DNS), 67/68 (DHCP), 69 (TFTP) etc.
- The UDP header consists of source port, destination port, length and checksum fields.

Here are some mnemonics to remember UDP:

- Uber Datagram Protocol
- Unreliable Datagram Protocol
- Useless Data Protocol (jokingly as it is unreliable!)

Some advantages and disadvantages of UDP:

Advantages:
- Fast speed and low overhead due to no connection establishment
- Simplicity of implementation as fewer functions are required

Disadvantages:
- No guarantee of delivery or order of packets
- Vulnerable to spoofing attacks as there is no verification of source
- Higher risk of errors as there is less error checking

Example applications: Online video streaming, Voice over IP (VoIP), DNS, DHCP, SNMP, TFTP, Multicasting

[Detailed diagrams and codes can be included here if required]

I hope this helps you learn about the UDP transport layer protocol. Let me know if you would like me to elaborate on any of the points or include additional details.